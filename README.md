
# Telegram Message Archiver

Telegram Message Archiver is a tool to archive messages from Telegram dialogs into a database.

## Features

- Connects to Telegram using Telethon
- Archives messages from Telegram dialogs
- Stores messages in a database using SQLAlchemy
- Provides CLI commands for initializing the database and running the archiver

## Requirements

- Python 3.8+
- MySQL (or any other SQLAlchemy-supported database)
- Telethon
- SQLAlchemy
- Click

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/telegram_messages_archiver.git
    cd telegram_messages_archiver
    ```

2. Install Poetry:
    ```sh
    pip install poetry
    ```

3. Install the required packages:
    ```sh
    poetry install
    ```

4. **Get Telegram API credentials**:
   - Go to [my.telegram.org](https://my.telegram.org) and log in with your phone number.
   - Navigate to **API development tools** and create a new application.
   - Copy the **API ID** and **API Hash**.

5. **Create a `.env` file**:
   - In the root of your project directory, create a file named `.env`.

## Configuration

- API_ID: Your Telegram API ID 
- API_HASH: Your Telegram API Hash
- PHONE: Your Telegram phone number
- MESSAGE_LIMIT: Limit of messages to fetch per dialog
- DSN: Data Source Name for the database
- DEBUG: Enable debug messages (true/false)

## Usage

```sh
poetry shell
```

1. Initialize the Database

   To initialize the database, run:
   ```sh
   python . initdb
   ```

2. Run the script:
   ```sh
   python .
   ```

## Troubleshooting

- **Session errors**: If you're prompted for 2FA, enter the password to complete the login.
- **Connection issues**: Ensure you have an active internet connection and correct API credentials.

## Acknowledgment
This project was started by [@MiguelTracelon] (https://www.github.com/MiguelTracelon)

Special thank to:
- Tacelon (https://tracelon.com) for initial realease
- People from SEAL (https://securityalliance.org/) for ideological support
## Notes

- **Privacy and Permissions**: Ensure you have permission to fetch and store messages, especially from groups and channels.
- **Rate Limits**: Avoid running the script too frequently to prevent triggering Telegram's rate limits.

## License

This project is open-source and available under the GPL v3 License.
