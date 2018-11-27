
import db
import json
from bson import json_util


def do_search(word):

    ind = db.indexes.find({"index": word})

    docs_list = []

    for i in ind:
        i.pop('_id', None)
        i.pop('index', None)
        docs_list.append(i)

    j = json.dumps(docs_list, default=json_util.default)

    # list of {context,url,point}
    return j
