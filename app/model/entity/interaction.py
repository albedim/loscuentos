from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Interaction(Base):
    __tablename__ = 'interactions'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    chapter_id = Column(Integer, ForeignKey('chapters.chapter_id'), primary_key=True)
    action = Column(Integer, nullable=False)
