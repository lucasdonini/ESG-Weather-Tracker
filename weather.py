from typing import Dict
from datetime import datetime

_MIN_FIELD_NAME = "min"
_MAX_FIELD_NAME = "max"
_AIR_HUMIDITY_FIELD_NAME = "air_humidity"
_DATE_FILED_NAME = "date"


class Weather:
    def __init__(self, min: int, max: int, air_humidity: float, date: datetime):
        self.min = min
        self.max = max
        self.air_humidity = air_humidity
        self.date = date

    def to_document(self):
        return {
            _MIN_FIELD_NAME: self.min,
            _MAX_FIELD_NAME: self.max,
            _DATE_FILED_NAME: self.date,
            _AIR_HUMIDITY_FIELD_NAME: self.air_humidity
        }

    def __str__(self):
        return f"Weather(max={self.max}, min={self.min}, date={self.date}, air_humidity={self.air_humidity})"


def from_document(doc: Dict[int, int, int, float]) -> Weather:
    return Weather(
        min=doc[_MIN_FIELD_NAME],
        max=doc[_MAX_FIELD_NAME],
        date=doc[_DATE_FILED_NAME],
        air_humidity=doc[_AIR_HUMIDITY_FIELD_NAME]
    )
