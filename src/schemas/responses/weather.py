from pydantic import BaseModel


class WeatherCityResponse(BaseModel):
    city: str
    temperature: float
