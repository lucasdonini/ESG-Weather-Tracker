from pymongo import MongoClient, DESCENDING
from typing import List
from weather import Weather, from_document, _DATE_FILED_NAME
import dotenv
import os

dotenv.load_dotenv()
client = MongoClient(os.getenv("DB_URL"))
db = client[os.getenv("DB_NAME")]
collection = db["weather"]


def save(weather: Weather):
    collection.insert_one(weather.to_document())


def load() -> List[Weather]:
    return [from_document(doc=data) for data in collection.find().sort(_DATE_FILED_NAME, DESCENDING)]
