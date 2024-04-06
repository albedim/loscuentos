from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.story_tag import StoryTagService
from app.utils.utils import arrayToJSON

storyTagRouter = APIRouter()