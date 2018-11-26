

import fileio
import search

from flask import Flask
app = Flask(__name__)

@app.route("/search/<word>")
def search_word(word):
    return search.make_search(word)

if __name__ == "__main__":

    fileio.parse_file("test.txt")

    print(search.make_search("Dark"))

    app.run(host="localhost")




