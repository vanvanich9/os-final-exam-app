from fastapi import APIRouter

from src.schemas import PingResponse

router = APIRouter()


@router.get('/')
def pingpong():
    return PingResponse()
