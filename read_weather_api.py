from weather import Weather
from datetime import datetime
import os
import requests

_MIN_TEMP = "temperature_2m_min"
_MAX_TEMP = "temperature_2m_max"
_HUMIDITY = "relative_humidity_2m_mean"


def make_request():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": os.getenv("LATITUDE"),
        "longitude": os.getenv("LONGITUDE"),
        "daily": f"{_MIN_TEMP},{_MAX_TEMP},{_HUMIDITY}"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    return {key: value[0] for key, value in data["daily"].items()}


def read_weather() -> Weather:
    data = make_request()
    return Weather(
        min=data[_MIN_TEMP],
        max=data[_MAX_TEMP],
        air_humidity=data[_HUMIDITY],
        date=datetime.now()
    )
