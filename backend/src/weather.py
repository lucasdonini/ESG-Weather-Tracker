from datetime import datetime
from pydantic import BaseModel

_MIN_FIELD_NAME = "min"
_MAX_FIELD_NAME = "max"
_AIR_HUMIDITY_FIELD_NAME = "air_humidity"
_DATE_FILED_NAME = "date"


class Weather(BaseModel):
    min: float
    max: float
    air_humidity: float
    date: datetime

    def to_document(self):
        return {
            _MIN_FIELD_NAME: self.min,
            _MAX_FIELD_NAME: self.max,
            _DATE_FILED_NAME: self.date,
            _AIR_HUMIDITY_FIELD_NAME: self.air_humidity
        }
