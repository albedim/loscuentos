from fastapi import APIRouter
from starlette.requests import Request
from app.configuration.config import templates
from app.services.social_link import SocialLinkService
from app.utils.utils import arrayToJSON

socialLinkRouter = APIRouter()