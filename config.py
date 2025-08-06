from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    ADMINS = list(map(int, os.getenv("ADMINS").split(","))) if os.getenv("ADMINS") else []

def is_admin(user_id: int) -> bool:
    return user_id in Config.ADMINS

config = Config()

