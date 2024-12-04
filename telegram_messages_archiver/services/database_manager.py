from telegram_messages_archiver.database import Database
from telegram_messages_archiver.models import Base


class DatabaseManager:

    @staticmethod
    def initdb():
        Base.metadata.drop_all(bind=Database.get_engine())
        Base.metadata.create_all(bind=Database.get_engine())
