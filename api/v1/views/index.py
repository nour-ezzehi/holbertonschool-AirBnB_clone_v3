#!/usr/bin/python3
"""the route status"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def get_status():
    """returns status ok"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def get_stats():
    """returns number of each objects by type"""

    from models import storage

    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
