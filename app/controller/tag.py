from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.tag import TagService
from app.utils.utils import arrayToJSON

tagRouter = APIRouter()