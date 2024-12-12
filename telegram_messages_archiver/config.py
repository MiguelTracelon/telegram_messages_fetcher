from dotenv import load_dotenv, dotenv_values

load_dotenv()
env = dotenv_values("../.env")


class Config:
    api_id = ""
    api_hash = ""
    phone = ""
    message_limit = ""
    dsn = ""
    debug = False

    @classmethod
    def init(cls, **kwargs):
        print("Initializing Config", kwargs)
        cls.api_id = kwargs.get("api_id") if kwargs.get("api_id") else env.get("API_ID")
        cls.api_hash = kwargs.get("api_hash") if kwargs.get("api_hash") else env.get("API_HASH")
        cls.phone = kwargs.get("phone") if kwargs.get("phone") else env.get("PHONE")
        cls.message_limit = kwargs.get("message_limit") if kwargs.get("message_limit") else env.get("MESSAGE_LIMIT")
        cls.dsn = kwargs.get("dsn") if kwargs.get("dsn") else env.get("DSN")
        cls.debug = kwargs.get("debug") if kwargs.get("debug") else env.get("DEBUG")
