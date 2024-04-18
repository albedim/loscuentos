from sqlalchemy import text
from app.configuration.config import sql
from app.model.entity.chapter import Chapter
from app.model.entity.favorite_tag import FavoriteTag
from app.model.entity.story import Story
from app.model.entity.story_tag import StoryTag
from app.model.entity.tag import Tag


class StoryRepository:

    @classmethod
    def getHomepageStories(cls, userId):
        stories = sql.query(Story).from_statement(
            text("SELECT stories.* "
                 "FROM stories "
                 "JOIN story_tags "
                 "ON stories.story_id = story_tags.story_id "
                 "JOIN favorite_tags "
                 "ON favorite_tags.tag_id = story_tags.tag_id "
                 "WHERE favorite_tags.user_id = :userId "
                 "ORDER BY score DESC").params(userId=userId)
        ).all()
        return stories