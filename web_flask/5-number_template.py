#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)


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


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """python is cool"""
    text = text.replace('_', ' ')
    return 'Python is {}'.format(text)


@app.route('/number/<int:n>')
def number(n):
    """n is a number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def n_template(n=None):
    """return a html content"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
