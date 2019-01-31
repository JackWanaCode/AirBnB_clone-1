#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False

dict_of_state = {}
all_states = storage.all("State")
for obj in all_states.values():
    dict_of_state[obj.__dict__['name']] = obj.__dict__['id']
list_of_state = list(sorted(dict_of_state.items()))


@app.route('/states_list')
@app.route('/states_list/<list_of_state>')
def print_state_list():
    """return a html content"""
    return render_template('7-states_list.html', list_of_state=list_of_state)


@app.teardown_appcontext
def teardown_storage(exception):
    """tear down"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
