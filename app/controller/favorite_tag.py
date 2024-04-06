from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.favorite_tag import FavoriteTagService
from app.utils.utils import arrayToJSON

favoriteTagRouter = APIRouter()