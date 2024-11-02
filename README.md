
# Telegram Message Fetcher

This project uses the Telethon library to connect to a Telegram user account and fetch messages from all dialogs (chats, groups, and channels). It saves the last 1000 messages (or any specified limit) from each dialog into a text file.

## Features
- Connects to a Telegram account using the Telegram API.
- Fetches messages from all private chats, groups, and channels.
- Saves messages to a file (`telegram_messages.txt`), with each dialog separated for easy reading.
- Includes detailed logging for debugging and troubleshooting.

## Requirements
- Python 3.7+
- A Telegram account with an API ID and API Hash (see instructions below).
- [Telethon](https://github.com/LonamiWebs/Telethon) library.
- [python-dotenv](https://github.com/theskumar/python-dotenv) library.

## Setup

1. **Clone the repository** (or create your project directory).
   ```bash
   git clone https://github.com/your-username/telegram-message-fetcher.git
   cd telegram-message-fetcher
   ```

2. **Install dependencies**:
   ```bash
   pip install telethon python-dotenv
   ```

3. **Get Telegram API credentials**:
   - Go to [my.telegram.org](https://my.telegram.org) and log in with your phone number.
   - Navigate to **API development tools** and create a new application.
   - Copy the **API ID** and **API Hash**.

4. **Create a `.env` file**:
   - In the root of your project directory, create a file named `.env`.
   - Add the following environment variables, replacing the values with your credentials:
     ```env
     API_ID=your_api_id
     API_HASH=your_api_hash
     PHONE=your_phone_number
     ```

## Usage

1. **Run the script**:
   ```bash
   python3 main.py
   ```

2. **Output**:
   - The script will fetch messages from all dialogs in your Telegram account and save them to `telegram_messages.txt`.
   - Each dialog will be separated by a header with the chat title and ID.
   - Only the last 1000 messages from each dialog will be saved (you can adjust this limit in the code).

## Configuration

- **MESSAGE_LIMIT**: Set the maximum number of messages to fetch per dialog. Adjust this in the code as needed.

## Example Output (telegram_messages.txt)

```plaintext
--- Messages from Example Chat (ID: 123456789) ---
2024-11-01 12:34:56 - 987654321: Hello, this is a test message.
2024-11-01 12:35:10 - 123456789: [Non-text message]
...

--- Messages from Example Group (ID: 987654321) ---
2024-11-01 15:00:00 - 654321987: Welcome to the group!
2024-11-01 15:10:05 - 123987456: [Non-text message]
...
```

## Troubleshooting

- **No messages in output file**: Ensure dialogs are being fetched and messages contain text or relevant content.
- **Session errors**: If you're prompted for 2FA, enter the password to complete the login.
- **Connection issues**: Ensure you have an active internet connection and correct API credentials.

## Notes

- **Privacy and Permissions**: Ensure you have permission to fetch and store messages, especially from groups and channels.
- **Rate Limits**: Avoid running the script too frequently to prevent triggering Telegram's rate limits.

## License

This project is open-source and available under the MIT License.
