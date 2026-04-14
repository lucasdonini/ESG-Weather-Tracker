from pymongo import MongoClient, DESCENDING
from typing import List
from .env import env
from .weather import (
    Weather,
    _DATE_FILED_NAME,
    _AIR_HUMIDITY_FIELD_NAME,
    _MAX_FIELD_NAME,
    _MIN_FIELD_NAME,
)

client = MongoClient(env.db_url)
db = client[env.db_name]
collection = db["weather"]


def save(weather_data: List[Weather]):
    transformed = [w.to_document() for w in weather_data]
    collection.insert_many(transformed)


def load() -> List[Weather]:
    return [
        Weather(
            min=data[_MIN_FIELD_NAME],
            max=data[_MAX_FIELD_NAME],
            air_humidity=data[_AIR_HUMIDITY_FIELD_NAME],
            date=data[_DATE_FILED_NAME],
        )
        for data in collection.find().sort(_DATE_FILED_NAME, DESCENDING)
    ]
