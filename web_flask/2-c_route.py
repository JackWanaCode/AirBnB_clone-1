#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_bnnb():
    """return Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """return HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def is_fun(text):
    """return c is fun"""
    c = text.replace('_', ' ')
    return 'C {}'.format(c)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
