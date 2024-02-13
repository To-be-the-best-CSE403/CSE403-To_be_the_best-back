import os
import json
from flask import jsonify

# from src.data.query import get_top_usage


def get_top_usage_api(top_n: int):
    # top_usage = get_top_usage(top_n)
    try:
        path = os.path.join("src", "api", "usage", f"usage100.json")
        with open(path) as file:
            usage = json.load(file)
            top_usage = usage[:top_n]
            return jsonify(top_usage)
    except FileNotFoundError:
        return jsonify({"error": f"No usage found for top {top_n}"}), 404
