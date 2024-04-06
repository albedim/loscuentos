from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.comment import CommentService
from app.utils.utils import arrayToJSON

commentRouter = APIRouter()