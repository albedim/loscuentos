from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.user import UserService
from app.utils.utils import arrayToJSON

userRouter = APIRouter()