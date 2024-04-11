#!/usr/bin/python3
""" RUN a Web Application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Prints a Message """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ Prints a Message"""
    return "C " + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_python(text="is cool"):
    """handles the python path"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """number path"""
    return f"{n} is a number"


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
