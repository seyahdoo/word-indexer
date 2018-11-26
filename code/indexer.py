import db

stop_words = ["", " ", "the", "and", "or", "but", "not", "for", "at", "nor", "to", "from"]


def add_index(context, url):
    words = context.split(" ")
    words = [word for word in words if word not in stop_words]

    i = 0
    for i in range(0, len(words)):
        obj = {"index": words[0], "context": context, "url": url, "point": i}
        db.indexes.insert_one(obj)
        rotate_right(words)

    return


def rotate_right(words):
    tmpcnt = words[len(words) - 1]
    for j in range(len(words) - 2, 0, -1):
        words[j + 1] = words[j]
    words[0] = tmpcnt