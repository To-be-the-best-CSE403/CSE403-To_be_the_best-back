from flask import jsonify
from src.data.query import get_top_usage


def get_top_usage_api(top_n: int):
    top_usage = get_top_usage(top_n)
    return jsonify(top_usage)
