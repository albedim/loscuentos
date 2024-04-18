from sqlalchemy import text
from app.configuration.config import sql
from app.model.entity.interaction import Interaction


class InteractionRepository:

    @classmethod
    def getInteractions(cls, chapter_id):
        interaction = sql.query(text("interaction")).from_statement(
            text("SELECT SUM(action) AS interaction "
                 "FROM interactions "
                 "WHERE chapter_id = :chapterId").params(chapterId=chapter_id)
        ).first()
        print(interaction[0])
        return interaction[0] if interaction[0] is not None else 0
