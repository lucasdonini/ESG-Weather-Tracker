from fastapi import FastAPI
from db_connection import load

app = FastAPI()

@app.get("/api/load")
def load_mongo_data():
    return load()
