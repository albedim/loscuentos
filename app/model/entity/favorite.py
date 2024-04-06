from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    story_id = Column(Integer, ForeignKey('stories.story_id'), primary_key=True)
