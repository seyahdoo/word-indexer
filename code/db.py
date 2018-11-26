

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["word-indexer"]
indexes: pymongo.collection.Collection = db["indexes"]

