from pydantic import BaseModel


class WeatherModel(BaseModel):
    city: str
    temperature: float
