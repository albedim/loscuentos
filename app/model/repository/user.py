from sqlalchemy import text
from app.configuration.config import sql
from app.model.entity.user import User


class UserRepository:

    @classmethod
    def getUserById(cls, user_id):
        user = sql.query(User).filter(User.user_id == user_id).first()
        return user
