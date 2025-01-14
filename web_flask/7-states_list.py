#!/usr/bin/python3
"""
Starts a flask app
listens to 0.0.0.0 on port 5000
"""
from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception=None):
    """Close the current session."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_state():
    """Render list of all states."""
    states_list = storage.all(State)
    return render_template('7-states_list.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
