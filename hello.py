# From http://flask.pocoo.org/

# run with
#
#  export FLASK_APP=<location>/hello.py
#  flask run

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<title>Hi!</title><h1>Hello World!</h1>"

