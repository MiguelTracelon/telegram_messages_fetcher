from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from telegram_messages_archiver.config import Config


class Database:
    engine = None
    sm = None
    Base = None

    @classmethod
    def init(cls):
        cls.engine = create_engine(Config.dsn, echo=False)
        cls.sm = sessionmaker(bind=cls.engine)
        cls.Base = declarative_base()

    @classmethod
    @contextmanager
    def get_db(cls) -> Session:
        db = cls.sm()
        try:
            yield db
        finally:
            db.close()

    @classmethod
    def get_engine(cls):
        return cls.engine
