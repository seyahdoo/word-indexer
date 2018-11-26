
import db


def add_index(context, url):
    #eleme yapılmalı burada -the,-and vs

    words = context.split(" ")
    indexlist = []
    cnt = context
    lastword = words[len(words) - 1]
    i = 0
    while cnt != context:
        words = cnt.split(" ")
        cnt = words[len(words) - 1]
        for j in range(0, len(words) - 2):
            cnt = cnt + words[j]
        obj = {"index": words[len(words)-1], "info": {"context": context, "url": url, "point": i}}
        db.indexes.insert_one(obj)
        i = i+1
        indexlist.append(obj)

    return