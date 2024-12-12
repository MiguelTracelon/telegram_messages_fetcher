from sqlalchemy import select
from sqlalchemy.orm import Session

from telegram_messages_archiver.database import Database
from telegram_messages_archiver.models import Dialog


class DialogManager:

    @classmethod
    def get_dialog_by_original_id(cls, dialog_original_id) -> Dialog | None:
        with Database.get_db() as db:  # type: Session
            stmt = (
                select(Dialog)
                .where(Dialog.dialog_original_id == dialog_original_id)
            )
            return db.scalars(stmt).first()

    @classmethod
    def save_dialog(cls, dialog: Dialog):
        with Database.get_db() as db:  # type: Session
            db.add(dialog)
            db.commit()
            return dialog.id
