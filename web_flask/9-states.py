#!/usr/bin/python3
"""script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


all_states = None
id = None

if getenv("HBNB_TYPE_STORAGE") == 'db':
    all_states = storage.all("State")
else:
    all_states = storage.all(State)


@app.route('/states')
@app.route('/states/<id>')
def print_city_list(id=None):
    """return a html content"""
    return render_template('9-states.html', all_states=all_states, id=id)


@app.teardown_appcontext
def teardown_storage(exception):
    """tear down"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
