from sqlalchemy import Column, Integer, String, ForeignKey, Date, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(14), nullable=False)
    email = Column(String(54), nullable=False)
    password = Column(String(54), nullable=False)
    bio = Column(String(150))
    created_on = Column(Date, nullable=False)
    image_path = Column(String(100), nullable=False)
    banner_path = Column(String(100), nullable=False)

