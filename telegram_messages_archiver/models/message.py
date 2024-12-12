from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column

from telegram_messages_archiver.models.base import Base


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    dialog_id: Mapped[int] = mapped_column(BigInteger)
    sender_id: Mapped[int] = mapped_column(BigInteger)
    dialog_original_id: Mapped[int] = mapped_column(BigInteger)
    message_original_id: Mapped[int] = mapped_column(BigInteger)
    date: Mapped[datetime]
    edit_date: Mapped[Optional[datetime]]
    message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"Message model, id: {self.id}, date: {self.date}, message_original_id: {self.message_original_id}"

