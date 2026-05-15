from fastapi import FastAPI
from scrape import run as scrape_mojo_movies
from logger import trigger_logs_save
app = FastAPI()

@app.get ("/")
def hello_world () :
    return {"hello": "world"}

@app.get("/abc")
def abc_view() :
    return {"data": [1,2,31]}

@app.post("/flask-scrape")
def flask_scrape_mojo_movies():
    trigger_logs_save()
    scrape_mojo_movies()
    return {"data": [1,2,31]}