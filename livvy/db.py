import pymongo

from config import MONGO_URL


database = pymongo.MongoClient(MONGO_URL)['notes']['notes']
