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

    def toJSON(self, **kvargs):
        obj = {
            'story_id': self.story_id,
            'name': self.name,
            'created_on': str(self.created_on),
            'author_id': self.author_id
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj