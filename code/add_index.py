def add_index(str, url):
    words = str.split(" ")
    indexlist = []

    lastword = words[words.len() - 1]
    while str.split(" ")[0] != lastword:
        lst = str.split(" ")
        str = lst[lst.len() - 1]
        for i in range(0, lst.len() - 2):
            str = str + lst[i]

    indexlist.add({"context": str, "url": url})

    index = "index"
    context = "context"
    url = "url"
    point = 5

    obj = {"index": index, "info": {"context": context, "url": url, "point": point}}

    return