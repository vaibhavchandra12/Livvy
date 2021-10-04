from pyrogram import filters , Client
import os 
from aiohttp import ClientSession
from config import API_ID, API_HASH, BOT_TOKEN
livvycmd = Client(
    'bot',
    api_id=os.environ.get('API_ID'),
    api_hash=os.environ['API_HASH'],
    bot_token=os.environ['BOT_TOKEN'],
    plugins=dict(root=f"livvy/plugins")
)

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from config import MONGO_URL

mongo_client = MongoClient(MONGO_URL)
db = mongo_client.livvy

aiohttpsession = ClientSession()


help_message = []
