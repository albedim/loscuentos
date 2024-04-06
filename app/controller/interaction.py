from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.interaction import InteractionService
from app.utils.utils import arrayToJSON

interactionRouter = APIRouter()