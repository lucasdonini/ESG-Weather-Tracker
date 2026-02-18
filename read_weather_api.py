from weather import Weather
from datetime import datetime, timedelta
import os
import requests

_MIN_TEMP = "temperature_2m_min"
_MAX_TEMP = "temperature_2m_max"
_HUMIDITY = "relative_humidity_2m_mean"


def request_today_data():
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


def request_past_data(start_date: datetime):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": os.getenv("LATITUDE"),
        "longitude": os.getenv("LONGITUDE"),
        "daily": f"{_MIN_TEMP},{_MAX_TEMP},{_HUMIDITY}",
        "start_date": start_date + timedelta(days=1),
        "end_date": datetime.now().date() - timedelta(days=1)
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()["daily"]
    return [
        Weather(
            min=data[_MIN_TEMP][index],
            max=data[_MAX_TEMP][index],
            air_humidity=data[_HUMIDITY][index],
            date=datetime.fromisoformat(data["time"][index])
        ) for index in range(len(data["time"]))
    ]


def read_todays_weather() -> Weather:
    data = request_today_data()
    return Weather(
        min=data[_MIN_TEMP],
        max=data[_MAX_TEMP],
        air_humidity=data[_HUMIDITY],
        date=datetime.now()
    )
