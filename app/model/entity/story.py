from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Story(Base):
    __tablename__ = 'stories'
    story_id = Column(Integer, primary_key=True)
    name = Column(String(84), nullable=False)
    created_on = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('users.user_id'))