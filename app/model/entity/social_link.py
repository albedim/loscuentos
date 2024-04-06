from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class SocialLink(Base):
    __tablename__ = 'social_links'
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    name = Column(String(24), primary_key=True)
    value = Column(String(54), nullable=False)
