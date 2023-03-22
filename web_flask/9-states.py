#!/usr/bin/python3
"""
Starts a flask app
listens to 0.0.0.0 on port 5000
"""
import os
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def cities_by_states():
    """
    Displays list of all cities by State objects in DBStorage.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Displays page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exception):
    """Remove the current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)