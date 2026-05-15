import os
import sys
import datetime
import requests
import pandas as pd
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)



def url_to_txt(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", 'w') as f:
                f.write(html_text)
        return html_text
    return None



def parse_and_extract(url, name='2020'):
    html_text = url_to_txt(url)
    if html_text == None:
        return False
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    # table_class = "#table"
    r_table = r_html.find(table_class)

    # print(r_table)
    table_data = []
    # table_data_dicts = []
    header_names = []
    if len(r_table) == 0:
        return False
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_cols = header_row.find('th')
    header_names = [x.text for x in header_cols]
    for row in rows[1:]:
        # print(row.text)
        cols = row.find("td")
        row_data = []
        row_dict_data = {}
        for i, col in enumerate(cols):
            # print(i, col.text, '\n\n')
            header_name = header_names[i]
            # row_dict_data[header_name] = col.text
            row_data.append(col.text)
        #table_data_dicts.append(row_dict_data)
        table_data.append(row_data)
    df = pd.DataFrame(table_data, columns=header_names)
    # df = pd.DataFrame(table_data_dicts)
    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join('data', f'{name}.csv')
    df.to_csv(filepath, index=False)
    return True

def run(start_year=None, years_ago=0):
    if start_year == None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    for i in range(0, years_ago+1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}/"
        finished = parse_and_extract(url, name=start_year)
        if finished:
            print(f"Finished {start_year}")
        else:
            print(f"{start_year} not finished")
        start_year -= 1



if __name__ == "__main__":
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 0
    run(start_year=start, years_ago=count)









































# now = datetime.datetime.now()
# year = now.year

# # def url_to_file (url, filename = "world.html"):
# #     r = requests.get(url)
# #     if r.status_code == 200:
# #         html_file = r.text
# #         with open(filename, "w") as f :
# #             f.write(html_file)
# #             return filename

# def url_to_text (url, filename = "world.html", save = False):
#     r = requests.get(url)
#     if r.status_code == 200:
#         html_text = r.text
#         if save == False:
#             with open(f" The IMDB in {year} year !", "w") as f :
#                 f.write(html_text)
#                 # return filename
#                 return html_text
           
# # url = "https://www.boxofficemojo.com"
# ##url = "https://www.boxofficemojo.com/date/" 
# # print(url_to_file(url))

# def scrape_and_csv (url, name="2026"):
#     html_text = url_to_text(url)
#     r_html  = HTML(html=html_text)

#     class_name1 = ".imdb-scroll-table"
#     class_name = "imdb-scroll-table"
#     # ".a-section a-spacing-none mojo-column"
#     r_table = r_html.find(class_name1)

#     table_data = []
#     header_names = []

#     #print(r_table)
#     if len(r_table) == 1:
#         table_text = r_table[0].text

#     rows  = r_table[0].find("tr")
#     #print(rows)
#     header = rows[0]
#     header_cols = header.find("th")
#     header_names = [x.text for x in header_cols]

#     for row in rows[1:]:
#         #print (row.text)
#         raw_data = []
#         cols = row.find("td")
#         for i, col in enumerate(cols) :
#             raw_data.append(col.text)
#             # print( i, col, "\n\n" )
#         table_data.append(raw_data)

#     #this_file = os.path.abspath(__file__)
#     BASE_DIR = os.path.dirname(__file__)
#     #BASE_DIR = os.path.dirname(this_file)
#     file_path = os.path.join(BASE_DIR, "data")
#     os.makedirs(file_path, exist_ok = True)
#     csv_path = os.path.join(file_path, f"{name}.csv")

#     df = pd.DataFrame(table_data, columns = header_names)
#     df.to_csv(csv_path, index = False)

#     # print(header_names)
#     # print(table_data)

# url = "https://www.boxofficemojo.com/daily/2026/" 
# scrape_and_csv(url)
