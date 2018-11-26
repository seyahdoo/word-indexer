
import add_index

def parse_file(file_path):
    # dark knight rises ; url223 ;
    file = open(file_path, "r")
    context = []
    for line in file:
        context = line.split(";")[0]
        url = line.split(";")[1]
        add_index.add_index(context,url)

    file.close()
