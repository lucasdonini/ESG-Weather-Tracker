from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.exceptions import HTTPException
from .db_connection import load

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")


@app.exception_handler(HTTPException)
def spa_handler(request, exc):
    if exc.status_code == 404:
        return FileResponse("dist/index.html")
    raise exc


@app.get("/api/load")
def load_mongo_data():
    return load()[::-1]
