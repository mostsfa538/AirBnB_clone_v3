#!/usr/bin/python3
""" Here goes every thing """
from flask import jsonify
from api.v1.views import app_views
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models import storage


@app_views.route('/status')
def status():
    """ get status """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """ get count for every model """
    classes = {"amenities": Amenity, "cities": City, "places": Place,
               "reviews": Review, "states": State, "users": User}
    data = {}

    for key, cls in classes.items():
        data[key.lower()] = storage.count(cls)

    return jsonify(data)
