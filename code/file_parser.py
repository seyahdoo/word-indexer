
import indexer
import os


def parse_file(file_path):
    # file format
    # dark knight rises ; url223 ;
    print("parsing file")

    size = os.path.getsize(file_path)
    if size > 20000000:
        print("input file size is too large, returning without processing")
        return

    file = open(file_path, "r")
    for line in file:
        context = line.split(";")[0]
        url = line.split(";")[1]
        indexer.add_index(context, url)

    file.close()
    return
