#!/usr/bin/python3
"""
A script that starts a Flask application:
Listening on 0.0.0.0:5000
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """"displays: Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays: HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """displays: C followed by the value
        of the text variable"""
    return "C %s" % text.replace('_', '')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """displays: Python followed by the value
        of the text variable"""
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """"displays 'n' if is an int"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays a page if n is an int"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
