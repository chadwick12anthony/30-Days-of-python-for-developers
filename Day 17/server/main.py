import os
import pandas as pd
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return{"Hello":"World!"}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(BASE_DIR, 'cache')
dataset = os.path.join(CACHE_DIR, 'movies-box-office-dataset-cleaned.csv')

@app.get("/box-office")
def read_box_office_nbrs():
    df = pd.read_csv(dataset)
    #return df.to_dict("Rank")
    #return df.set_index('Rank').to_dict(orient='index')
    #return df.to_dict(orient='records')
    
    print(df.to_json(orient='records', indent=2))
    return df.set_index('Rank').to_dict(orient='index')