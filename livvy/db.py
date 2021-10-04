import pymongo

from config import MONGO_URL

mongo_client = MongoClient(MONGO_URL)
db = mongo_client.wbb
