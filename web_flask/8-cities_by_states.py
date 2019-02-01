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

list_of_state = []
list_of_city = []
dic = {}
all_states = storage.all("State")


if getenv("HBNB_TYPE_STORAGE") == 'db':
    for st in (storage._DBStorage__session.query(State).
               order_by(State.name).all()):
        list_of_state.append([st.id, st.name])
        for ct in (storage._DBStorage__session.query(City).order_by(City.name).
                   filter(City.state_id == st.id).all()):
            list_of_city.append(ct)
        dic[st.name] = list_of_city
        list_of_city = []


@app.route('/cities_by_states')
def print_state_list():
    """return a html content"""
    return render_template('8-cities_by_states.html',
                           list_of_state=list_of_state, dic=dic)


@app.teardown_appcontext
def teardown_storage(exception):
    """tear down"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
