from weather import Weather
from datetime import date, datetime
import os
import requests

_MIN_TEMP = "temperature_2m_min"
_MAX_TEMP = "temperature_2m_max"
_HUMIDITY = "relative_humidity_2m_mean"


def read_weather_api(start_date: date, end_date: date):
    if start_date > end_date: raise ValueError("start date is after end date")
    
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": os.getenv("LATITUDE"),
        "longitude": os.getenv("LONGITUDE"),
        "daily": f"{_MIN_TEMP},{_MAX_TEMP},{_HUMIDITY}",
        "start_date": start_date,
        "end_date": end_date
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
