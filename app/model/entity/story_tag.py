from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class StoryTag(Base):
    __tablename__ = 'story_tags'
    tag_id = Column(Integer, ForeignKey('tags.tag_id'), primary_key=True)
    story_id = Column(Integer, ForeignKey('stories.story_id'), primary_key=True)
