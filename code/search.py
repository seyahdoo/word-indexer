
import pprint

import db

import json


def make_search(word):

    # indexes.insert_one({"word":"rises"})
    ind = db.indexes.find({"word": word})

    # print(json.dumps(ind))

    # list of {context,url,point}
    return