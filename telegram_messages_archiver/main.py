import click
from telethon.errors import SessionPasswordNeededError

from cmd import root
from config import Config
from telegram_messages_archiver.database import Database


# Load environment variables
# load_dotenv()
# api_id = os.getenv("API_ID")
# api_hash = os.getenv("API_HASH")
# phone = os.getenv("PHONE")

# Initialize the client
# client = TelegramClient("session_name", api_id, api_hash)

@click.command()
@click.version_option(version="0.1.0", prog_name="Telegram Message Archiver")
@click.option("--api_id", envvar="API_ID", help="Telegram API ID")
@click.option("--api_hash", envvar="API_HASH", help="Telegram API HASH")
@click.option("--phone", envvar="PHONE", help="Telegram phone number")
@click.option("--message_limit", envvar="MESSAGE_LIMIT", help="Telegram message limit")
@click.option("--dsn", envvar="DSN", help="DSN")
def hello(**kwargs):
    Config.init(**kwargs)

    # client = TelegramClient("session_name", api_id, api_hash)
    # with client:
    #     client.loop.run_until_complete(run(client, phone))


async def run(client, phone):
    # Connect to the Telegram account
    await client.start(phone)
    print("Connected to Telegram")

    with Database().get_db() as db:
        db.flush()

    # Request 2FA code if enabled
    if await client.is_user_authorized() is False:
        try:
            await client.sign_in(phone=phone)
        except SessionPasswordNeededError:
            password = input("Please enter your 2FA password: ")
            await client.sign_in(password=password)

    MESSAGE_LIMIT = 1
    # Open file to save messages
    with open("../telegram_messages.txt", "w", encoding="utf-8") as f:
        # Iterate over all dialogs (chats, groups, channels)
        async for dialog in client.iter_dialogs():
            entity = dialog.entity
            chat_title = entity.title if hasattr(entity, "title") else entity.username or "Unknown Chat"
            print(f"Fetching messages from {chat_title} (ID: {entity.id}, Type: {type(entity)})")  # Log dialog details

            f.write(f"--- Messages from {chat_title} (ID: {entity.id}) ---\n")

            # Fetch messages in the current chat
            try:
                async for message in client.iter_messages(entity, limit=MESSAGE_LIMIT):
                    # Print detailed message data for debugging
                    print(f"Message fetched from {chat_title}:")
                    print(f"    Date: {message.date}")
                    print(f"    Sender ID: {message.sender_id}")
                    print(f"    Message ID: {message.id}")
                    print(f"    Content: {message.text or '[Non-text message]'}")
                    print(f"    Full message object: {message}")

                    # Save message data to file
                    f.write(f"{message.date} - {message.sender_id}: {message.text or '[Non-text message]'}\n")
                f.write("\n")  # Separate between chats
            except Exception as e:
                print(f"Error retrieving messages from {chat_title}: {e}")
                continue  # Skip to the next dialog in case of error

    print("Messages saved to telegram_messages.txt")

# Run the script
# with client:
#     client.loop.run_until_complete(hello())


# if __name__ == '__main__':
#     root()