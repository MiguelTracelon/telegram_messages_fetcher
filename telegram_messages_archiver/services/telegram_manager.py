import logging
from time import sleep

from telethon import TelegramClient

from telegram_messages_archiver.config import Config
from telegram_messages_archiver.models import Dialog
from telegram_messages_archiver.services import DialogManager, MessageManager


class TelegramManager:

    @classmethod
    def connect_to_telegram_and_run(cls):
        api_id = Config.api_id
        api_hash = Config.api_hash
        phone = Config.phone

        logging.debug("Connecting to Telegram server...")
        client = TelegramClient("session_name", api_id, api_hash)

        client.start(phone)
        logging.debug("Connected to Telegram server.")

        with client:
            client.loop.run_until_complete(cls.run(client))

    @classmethod
    async def run(cls, client):
        async for d in client.iter_dialogs():
            logging.info("Telegram dialog: %s", d.name)
            dialog = DialogManager.get_dialog_by_original_id(d.id)
            if dialog is None:
                logging.debug("Save new dialog: %s", d.name)
                dialog = Dialog(
                    dialog_original_id=d.id,
                    name=d.name,
                    archived=d.archived
                )
                DialogManager.save_dialog(dialog)
            await cls.save_messages(
                tg_client=client,
                dialog_entity=d.entity,
                dialog_id=dialog.id,
                dialog_original_id=d.id
            )

            return

    @classmethod
    async def save_messages(cls, tg_client, dialog_entity, dialog_id, dialog_original_id):
        last_message = MessageManager.get_last_message(dialog_original_id=dialog_original_id)

        last_id = 0
        if last_message:
            logging.debug(last_message)
            logging.debug(last_message.id)
            logging.debug(last_message.date)
            logging.debug(last_message.dialog_original_id)
            logging.debug(last_message.message_original_id)

            last_id = last_message.message_original_id

        logging.debug(f"Getting messages from last id: {last_id}")

        original_messages = await tg_client.get_messages(
            entity=dialog_entity,
            limit=int(Config.message_limit),
            reverse=True,
            min_id=last_id
        )

        logging.debug(f"Count of messages: {len(original_messages)}", )

        if not original_messages:
            return

        MessageManager.save_messages(cls.convert_original_messages_to_local(
            dialog_id=dialog_id,
            dialog_original_id=dialog_original_id,
            original_messages=original_messages
        ))

        # sleep(1)
        #
        # await cls.save_messages(tg_client, dialog_entity, dialog_id, dialog_original_id)

    @classmethod
    def convert_original_messages_to_local(cls, dialog_id, dialog_original_id, original_messages) -> [dict]:
        new_messages = []
        for om in original_messages:
            logging.debug(f"Got original message: {om}")
            message = {
                "dialog_id": dialog_id,
                "sender_id": om.sender_id,
                "dialog_original_id": dialog_original_id,
                "message_original_id": om.id,
                "message": om.text,
                "date": om.date,
                "edit_date": om.edit_date,
            }
            new_messages.append(message)

        return new_messages
