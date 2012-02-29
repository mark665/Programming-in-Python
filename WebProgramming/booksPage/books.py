"""
Minimal Flask + forms demo

Send HTML page that echoes message from HTTP request
To get started, point browser at echo_flask.html
"""

from flask import Flask, render_template, request
from bookdb import BookDB

# No need for message page
# Flask converts view function return string to HTML page

app = Flask(__name__)

app.debug = True # development only - remove on production machines

booksDB = BookDB ()

# View functions generate HTTP responses including HTML pages and headers

@app.route('/books.html')
def bookList():
    return render_template('bookslist.html',titles = booksDB.titles())
#    return form_page

@app.route('/abook/<book_id>')
def bookInfo(book_id):
    return render_template('book.html', thisBook = booksDB.title_info(book_id))
#    return from_page


# No function needed for other routes - Flask will send 404 page

if __name__ == '__main__':
    app.run()

