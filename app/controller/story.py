from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.story import StoryService
from app.utils.utils import arrayToJSON

storyRouter = APIRouter()