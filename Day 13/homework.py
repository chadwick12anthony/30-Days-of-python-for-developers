import requests
import pandas as pd
from requests_html import HTML
import time
import os
from datetime import datetime

# ==================== CONFIGURATION ====================
API_KEY = "3f6294753d3a2aad33fb73b58e7504cf"
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, 'movie_data')
os.makedirs(DATA_DIR, exist_ok=True)

# ==================== PART 1: SCRAPING ====================
def scrape_box_office(url):
    """Scrape box office data from Box Office Mojo"""
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    html = HTML(html=response.text)
    table = html.find(".imdb-scroll-table", first=True)
    
    if not table:
        return None
    
    rows = table.find("tr")
    headers = [th.text for th in rows[0].find("th")]
    
    data = []
    for row in rows[1:]:
        cells = row.find("td")
        if len(cells) == len(headers):
            row_data = {}
            for i, cell in enumerate(cells):
                row_data[headers[i]] = cell.text.strip()
            data.append(row_data)
    
    return pd.DataFrame(data)

# ==================== PART 2: API ENRICHMENT ====================
def enrich_with_tmdb(movie_title):
    """Get movie details from TMDB API"""
    clean_title = movie_title.split('(')[0].strip()
    
    # Search for the movie
    search_url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': API_KEY,
        'query': clean_title
    }
    
    response = requests.get(search_url, params=params)
    if response.status_code != 200:
        return None
    
    results = response.json().get('results', [])
    if not results:
        return None
    
    movie_id = results[0]['id']
    time.sleep(0.5)
    
    # Get full details
    detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    detail_response = requests.get(detail_url, params={'api_key': API_KEY})
    
    if detail_response.status_code != 200:
        return None
    
    details = detail_response.json()
    
    return {
        'tmdb_id': movie_id,
        'tmdb_title': details.get('title'),
        'release_date': details.get('release_date'),
        'runtime': details.get('runtime'),
        'budget': details.get('budget'),
        'revenue': details.get('revenue'),
        'rating': details.get('vote_average'),
        'genres': [g['name'] for g in details.get('genres', [])],
        'overview': details.get('overview')[:100] + '...' if details.get('overview') else None
    }

# ==================== PART 3: COMBINE EVERYTHING ====================
def main():
    # Scrape box office data
    url = "https://www.boxofficemojo.com/daily/2026/"
    box_office_df = scrape_box_office(url)
    
    if box_office_df is None:
        print(" Failed to scrape data")
        return
    
    # Get unique movie titles
    movie_titles = box_office_df['#1 Release'].unique()
    
    # Enrich each movie with TMDB data
    enriched_data = []
    failed = []
    
    for title in movie_titles:
        movie_info = enrich_with_tmdb(title)
        if movie_info:
            movie_info['scraped_title'] = title
            enriched_data.append(movie_info)
        else:
            failed.append(title)
    
    # Create enriched DataFrame
    enriched_df = pd.DataFrame(enriched_data)
    
    # Save files
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    movies_file = os.path.join(DATA_DIR, f'enriched_movies_{timestamp}.csv')
    enriched_df.to_csv(movies_file, index=False)
    
    # Merge with box office data
    merged = box_office_df.copy()
    for idx, row in enriched_df.iterrows():
        merged.loc[merged['#1 Release'] == row['scraped_title'], 
                   'tmdb_rating'] = row['rating']
        merged.loc[merged['#1 Release'] == row['scraped_title'], 
                   'tmdb_genres'] = str(row['genres'])
    
    final_file = os.path.join(DATA_DIR, f'complete_movie_data_{timestamp}.csv')
    merged.to_csv(final_file, index=False)
    
    # Minimal completion message
    print(f"Complete: {len(enriched_data)}/{len(movie_titles)} movies enriched")
    print(f"Files saved in {DATA_DIR}")

if __name__ == "__main__":
    main()