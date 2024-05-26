#!/usr/bin/python3
""" Here goes every thing """
from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app_views.route('/status')
def status():
    """ get status """
    return jsonify({"status": "OK"})
