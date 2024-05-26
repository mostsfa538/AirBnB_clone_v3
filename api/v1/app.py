#!/usr/bin/python3
""" Here goes every thing """
import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
<<<<<<< HEAD
def teardown_db(exception):
    """closes the storage on teardown"""
=======
def treardown(err):
    """  close """
>>>>>>> 9871ece05a48ef978f8b9d04d9dc8fe41a331df7
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """not_found"""
    return jsonify({"error": "Not found"}), 404


<<<<<<< HEAD
if __name__ == '__main__':
=======
if __name__ == "__main__":
>>>>>>> 9871ece05a48ef978f8b9d04d9dc8fe41a331df7
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(host=host, port=port, threaded=True)
