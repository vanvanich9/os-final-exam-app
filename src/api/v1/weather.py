from fastapi import APIRouter, Depends

from src.schemas import WeatherCityResponse
from src.services import WeatherService, get_weather_service


router = APIRouter()


@router.get('/{city}')
def get_weather_by_city(
    city: str,
    weather_service: WeatherService = Depends(get_weather_service),
):
    weather_model = weather_service.get_weather_by_city(city)
    return WeatherCityResponse(
        city=weather_model.city,
        temperature=weather_model.temperature,
    )
