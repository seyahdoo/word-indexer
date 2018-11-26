
import  pymongo

def parse_file(file_uri):
    # dark knight rises ; url223 ;



    pass



client = MongoClient('mongodb://localhost:27017/')
db = client["word_indexer"]
indexes: pymongo.collection.Collection = db["indexes"]

def add_index(context: str, url):

    words = context.split(" ")

    i = 0
    for w in words:
        #indexes.insert_one({"word":w,"link":{"context":context,"url":url}})

        i += 1


    return



def make_search(word):



    # list of {context,url,point}
    pass




if __name__ == "__main__":

    # while true
    # add_index





    pass




