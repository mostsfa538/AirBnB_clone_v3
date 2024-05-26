#!/usr/bin/python3
""" Here goes every thing """
<<<<<<< HEAD
from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app_views.route('/status')
def status():
    """ get status """
=======
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ get the status """
>>>>>>> 9871ece05a48ef978f8b9d04d9dc8fe41a331df7
    return jsonify({"status": "OK"})
