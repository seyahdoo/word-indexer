
import  pymongo

import pprint


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["word_indexer"]
indexes: pymongo.collection.Collection = db["indexes"]

def make_search(word):

    # indexes.insert_one({"word":"rises"})
    y = indexes.find({"word":word})

    pprint.pprint(y)

    for t in y:
        pprint.pprint(t)
        pass


    # list of {context,url,point}
    pass