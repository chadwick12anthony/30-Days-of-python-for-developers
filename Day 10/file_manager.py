import os 

filepath = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(filepath)

fpath = os.path.join(BASE_DIR, "templetes", "email.txt")
content = ""

with open(fpath, "r") as file :
    content = file.read()

print(content.format(name = "Юлия Сергеевна Кровьякова"))