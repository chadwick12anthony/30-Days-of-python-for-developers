import os 
import requests
import shutil
from download_utils import download_file

file_dir = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(file_dir)

DOWNLOAD_DIR = os.path.join(BASE_DIR, "Downloads")
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

download_to_url = os.path.join(DOWNLOAD_DIR, "1.jpg")

url = "https://wowprofi.ru/src/Frontend/Files/Cache/media_library_thumbnail_small_2/" \
"src/Frontend/Files/MediaLibrary/04/voen-academy-mojayskogo.jpg"

r = requests.get(url, stream = True)
r.raise_for_status() #200

with open(download_to_url, "wb") as f :
    f.write(r.content)

# dl_filename = os.path.basename(url) #endname
# new_dl_filename = os.path.join(DOWNLOAD_DIR, dl_filename)

# with requests.get(url, stream=True) as r:
#     with open(new_dl_filename, "wb") as file_object :
#         shutil.copyfileobj(r.raw, file_object)

download_file(url, DOWNLOAD_DIR)