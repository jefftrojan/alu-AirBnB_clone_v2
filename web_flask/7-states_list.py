#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask, render_template, request
from os import getenv
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Function that displays a HTML page """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Function that removes the current SQLAlchemy Session """
    storage.close()

if __name__ == '__main__':
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True)
