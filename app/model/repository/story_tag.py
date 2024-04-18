from sqlalchemy import text
from app.configuration.config import sql
from app.model.entity.story_tag import StoryTag
from app.model.entity.tag import Tag


class StoryTagRepository:

    @classmethod
    def getTags(cls, story_id):
        tags = sql.query(Tag).join(StoryTag, StoryTag.tag_id == Tag.tag_id).filter(StoryTag.story_id == story_id).all()
        return tags