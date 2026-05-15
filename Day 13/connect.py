import requests
import pprint
import pandas as pd 

api_key = "3f6294753d3a2aad33fb73b58e7504cf"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzZjYyOTQ3NTNkM2EyYWFkMzNmYjczYjU4ZTc1MDRjZiIsIm5iZiI6MTc3MzQwOTc3My44NTksInN1YiI6IjY5YjQxNWVkZjhhZmE2ZjA0MzRhNmY2NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Sc52kGCYLhXd1CerNsr4HINuRugBKEAN8OKY2yQgeU0"
"""
https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}

"""

movie_id = 550
tmdb_version = "3"
base_api_url = f"https://api.themoviedb.org/{tmdb_version}"
movie_path = f"/movie/{movie_id}"
endpoint_path = f"{base_api_url}{movie_path}?api_key={api_key}"

# r = requests.get(endpoint_path)
# print(r.status_code)


######################## v4 

movie_id = 550
tmdb_version_v4 = "3"
base_api_url = f"https://api.themoviedb.org/{tmdb_version_v4}"
movie_path = f"/movie/{movie_id}"

headers = {
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json; charset=utf-8'
}
endpoint_path = f"{base_api_url}{movie_path}" #?api_key={api_key}"
r = requests.get(endpoint_path, headers=headers)
# pprint.pprint(r.json())
# print(r.status_code, "\n\n\n\n\n\n\n\n\n")

movie_id = 550
endpoint_version = "3"
base_api_url = f"https://api.themoviedb.org/{endpoint_version}"
search_path = f"/search/movie"

search_query ="Avatar"
endpoint_path = f"{base_api_url}{search_path}?api_key={api_key}&query={search_query}"
r = requests.get(endpoint_path)
# pprint.pprint(r.json())
# print(endpoint_path)



if r.status_code in range (200, 299):
    data = r.json()
    results_form = data.keys() 
    print(results_form) # dict_keys(['page', 'results', 'total_pages', 'total_results'])
    results = data['results'] # List of dicts
    

    if len(results) > 0:
        movies_id = set()
        for result in results:
            _id = result['id']
            title = result['title']
            print(f"{_id} - {title}")
            movies_id.add(_id)
        print(list(movies_id))


movie_data = []
csv_doc = "movies.csv"
for movie_id in list(movies_id):
    tmdb_version = "3"
    base_api_url = f"https://api.themoviedb.org/{tmdb_version}"
    movie_path = f"/movie/{movie_id}"
    endpoint_path = f"{base_api_url}{movie_path}?api_key={api_key}"
    
    r = requests.get(endpoint_path)
    if r.status_code  in range (200,299):
        data = r.json()
        movie_data.append(data)
    print(movie_data)
df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(csv_doc, index=False)