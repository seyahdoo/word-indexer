

import fileio
import search

from flask import Flask
app = Flask(__name__)

@app.route("/search/<word>")
def search_word(word):
    return search.do_search(word)

if __name__ == "__main__":

    fileio.parse_file("test-data.txt")

    app.run(host="localhost")




