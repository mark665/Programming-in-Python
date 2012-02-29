"""
Minimal Flask + forms demo

Send HTML page that echoes message from HTTP request
To get started, point browser at echo_flask.html
"""

from flask import Flask, render_template, request
import copy

# No need for message page
# Flask converts view function return string to HTML page

app = Flask(__name__)

app.debug = True # development only - remove on production machines

messages = []

# View functions generate HTTP responses including HTML pages and headers

@app.route('/echo_flask.html')
def form():
    return render_template('form.html')
#    return form_page

@app.route('/echo_flask.py')
def message_page():
    # Flask Quickstart suggests request.form should work, but here it is empty
    # Flask converts return string to HTML page
    messages.insert(0,request.args['message'])
    return render_template('response.html', messages=copy.deepcopy(messages))
#    return 'Message: %s' % ("<br> Previous Message : ".join(messages))

# No function needed for other routes - Flask will send 404 page

if __name__ == '__main__':
    app.run()

