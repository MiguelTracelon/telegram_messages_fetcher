import logging
import colorlog
from logging.handlers import RotatingFileHandler

from telegram_messages_archiver.config import Config


class Logger:
    @classmethod
    def init(cls):
        logger = logging.getLogger()

        if Config.debug:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)

        file_handler = RotatingFileHandler(filename="logs/telegram_messages_archiver.log", maxBytes=1024 * 1024 * 100, backupCount=10)
        file_formatter = logging.Formatter('%(asctime)s %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s')
        file_handler.setFormatter(file_formatter)

        stdout_handler = logging.StreamHandler()
        stdout_formatter = colorlog.ColoredFormatter('%(log_color)s %(asctime)s %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s')
        stdout_handler.setFormatter(stdout_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)
