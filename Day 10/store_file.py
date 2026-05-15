import os 

file_dir = os.path.dirname(os.path.abspath(__file__))
files_dir = os.path.join(file_dir, "images")

print(os.path.exists(files_dir))

os.makedirs(files_dir,exist_ok=True)

images = range(0,12)
for i in images:
    fname = f"{i}.txt"
    if os.path.exists(os.path.join(files_dir, fname)):
        print(f"Skipped {fname} already exists")
        continue
    with open(os.path.join(files_dir, fname), "w") as f :
        f.write("Красотулька моя что с тобой ?")
        print(f" In {os.path.dirname(os.path.join(files_dir, fname))} created {fname}.txt and written text to it !")
