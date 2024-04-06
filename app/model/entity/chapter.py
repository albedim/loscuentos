from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Chapter(Base):
    __tablename__ = 'chapters'
    chapter_id = Column(Integer, primary_key=True)
    content = Column(String(1500), nullable=False)
    created_on = Column(Date, nullable=False)