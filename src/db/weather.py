from random import randint

from src.models import WeatherModel

class WeatherDatabase:
    """Weather database simulation."""

    def get_weather_by_city(self, city: str) -> WeatherModel:
        temperature = float(f'{randint(-40, 40)}.{randint(0, 9)}')
        return WeatherModel(city=city, temperature=temperature)


weather_database = WeatherDatabase()
