import db


def add_index(context, url):
    # eleme yapılmalı burada -the,-and vs

    words = context.split(" ")
    indexlist = []
    i = 0
    for i in range(0, len(words)):
        obj = {"index": words[0], "context": context, "url": url, "point": i}
        rotate_right(words)
        db.indexes.insert_one(obj)
        indexlist.append(obj)

    return


def rotate_right(words):
    tmpcnt = words[len(words) - 1]
    for j in range(len(words) - 2, 0, -1):
        words[j + 1] = words[j]
    words[0] = tmpcnt