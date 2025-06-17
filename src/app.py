from fastapi import FastAPI

from src.api.ping import router as ping_router
from src.api.v1.weather import router as weather_router


app = FastAPI()
app.include_router(ping_router, prefix='/api/ping')
app.include_router(weather_router, prefix='/api/v1/weather')
