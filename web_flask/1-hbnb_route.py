#!/usr/bin/python3
"This is a line of text"
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    "this is a line of text"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    "this is a line of text"
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
