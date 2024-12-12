from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from telegram_messages_archiver.models.base import Base


class Dialog(Base):
    __tablename__ = 'dialogs'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    dialog_original_id: Mapped[int] = mapped_column(BigInteger)
    archived: Mapped[bool]
    name: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f'<Dialog id={self.id} name={self.name}>'
