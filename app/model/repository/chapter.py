from sqlalchemy import text
from sqlalchemy.sql.functions import random

from app.configuration.config import sql
from app.model.entity.chapter import Chapter


class ChapterRepository:

    @classmethod
    def getRandomChapter(cls, storyId):
        chapter = sql.query(Chapter).filter(Chapter.story_id == storyId).order_by(random()).first()
        return chapter
