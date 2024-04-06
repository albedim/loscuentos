from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.chapter import ChapterService
from app.utils.utils import arrayToJSON

chapterRouter = APIRouter()