from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db_connection import load

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/api/load")
def load_mongo_data():
    return load()[::-1]
