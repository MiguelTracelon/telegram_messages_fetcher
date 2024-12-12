from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from telegram_messages_archiver.database import Database
from telegram_messages_archiver.models import Message


class MessageManager:

    @staticmethod
    def get_last_message(dialog_original_id) -> Message | None:
        with Database.get_db() as db:  # type: Session
            stmt = (
                select(Message)
                .where(Message.dialog_original_id == dialog_original_id)
                .order_by(Message.message_original_id.desc())
            )
            return db.scalars(stmt).first()

    @staticmethod
    def save_messages(messages):
        with Database.get_db() as db:  # type: Session
            db.execute(
                insert(Message),
                messages
            )
            db.commit()
