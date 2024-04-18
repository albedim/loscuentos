from sqlalchemy import text
from app.configuration.config import sql
from app.model.repository.chapter import ChapterRepository
from app.model.repository.interaction import InteractionRepository
from app.model.repository.story import Story, StoryRepository
from app.model.repository.story_tag import StoryTagRepository
from app.model.repository.user import UserRepository


class StoryService:

    @classmethod
    def getHomepageStories(cls, userId):
        stories = StoryRepository.getHomepageStories(userId)
        newStories = []
        for item in stories:
            chapter = ChapterRepository.getRandomChapter(item.story_id)
            user = UserRepository.getUserById(item.author_id)
            tags = StoryTagRepository.getTags(item.story_id)
            interaction = InteractionRepository.getInteractions(chapter.chapter_id)
            newStories.append({
                "story":item,
                "author": user,
                "tags":tags,
                "chapter":chapter,
                "interaction": interaction
            })
        return newStories
