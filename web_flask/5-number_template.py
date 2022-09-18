#!/usr/bin/python3
"This is a line of text"
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    "this is a line of text"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    "this is a line of text"
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def lan(text):
    "this is a line of text"
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def fun(text="is cool"):
    "this is a line of text"
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def func(n):
    "this is a line of text"
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def funct(n):
    "this is a line of text"
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
