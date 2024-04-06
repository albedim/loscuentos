from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.favorite import FavoriteService
from app.utils.utils import arrayToJSON

favoriteRouter = APIRouter()