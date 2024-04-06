from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class FavoriteTag(Base):
    __tablename__ = 'favorite_tags'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tags.tag_id'), primary_key=True)
    score = Column(Integer, nullable=False)
