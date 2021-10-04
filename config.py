import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


OWNER_NAME = getenv("OWNER_NAME", "KabeerxD")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RhythmOfficial")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(os.environ.get("OWNER_ID"))
MONGO_URL = os.environ.get("MONGO_URL")
BOT_USERNAME = getenv("BOT_USERNAME")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "RhythmOff")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
BOT_ID = int(os.environ.get("BOT_ID"))
