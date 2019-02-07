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
all_ame = None
all_places = None
id = None

if getenv("HBNB_TYPE_STORAGE") == 'db':
    all_states = storage.all("State")
    all_ame = storage.all("Amenity")
    all_places = storage.all("Place")
else:
    all_states = storage.all(State)
    all_ame = storage.all(Amenity)
    all_places = storage.all(Place)


@app.route('/hbnb_filters')
def print_city_list():
    """return a html content"""
    return render_template('10-hbnb_filters.html', all_states=all_states,
                            all_ame=all_ame, all_places=all_places)


@app.teardown_appcontext
def teardown_storage(exception):
    """tear down"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
