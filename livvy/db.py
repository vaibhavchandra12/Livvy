from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

from config import MONGO_URL

mongo_client = MongoClient(MONGO_URL)
db = mongo_client.livvy
