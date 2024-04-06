from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    chapter_id = Column(Integer, ForeignKey('chapters.chapter_id'), nullable=False)
    content = Column(String(250), nullable=False)
    parent_comment_id = Column(Integer, ForeignKey('comments.comment_id'))
