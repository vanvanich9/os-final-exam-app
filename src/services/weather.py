from functools import lru_cache

from src.db import WeatherDatabase, weather_database
from src.models import WeatherModel


class WeatherService:
    def __init__(self, db: WeatherDatabase):
        self.db = db

    def get_weather_by_city(self, city: str) -> WeatherModel:
        weather_model = self.db.get_weather_by_city(city)
        return weather_model


@lru_cache()
def get_weather_service():
    return WeatherService(weather_database)
