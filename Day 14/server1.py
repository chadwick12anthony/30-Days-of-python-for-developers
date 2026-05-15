from flask import Flask
from scrape import run as scrape_mojo_movies
from logger import trigger_logs_save

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def post_flask():
    return "This is flask !"


@app.route("/abc", methods = ['GET'])
def post_Flask():
    return "This is capital Flask !"

@app.route("/flask-scrape", methods = ['POST'])
def flask_scrape_mojo_movies():
    trigger_logs_save()
    scrape_mojo_movies()
    return{"data":[1,2,31]}
    #return "This flask scrape was successfully done!"