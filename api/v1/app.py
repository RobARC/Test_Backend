#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(400)
def not_found(error) -> str:
    """Not found handler."""
    return jsonify({"error": error.description}), 400


@app.before_request
def validation_query():
    """method to validate query."""

    param = request.args.get("card_number")

    try:
        card_info = param.replace(" ", "")

        request.card_number = card_info
    except Exception:
        abort(400, description="Query param no valid")


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=True)
