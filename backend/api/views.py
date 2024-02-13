from flask import Blueprint, request, jsonify
from src.api.teambuilder.teambuilder_api import get_team
from src.api.usage.usage_api import get_top_usage_api

views = Blueprint("views", __name__)


@views.route("/home")
def api_home():
    return "Hello, World!"


@views.route("/teambuilder", methods=["GET"])
def api_teambuilder():
    archetype = request.args.get("archetype")
    if not archetype:
        return jsonify({"error": "Teambuilder archetype parameter is missing"}), 400

    return get_team(archetype)


@views.route("/usage-rate", methods=["GET"])
def api_usage_rate():
    n = request.args.get("n")
    if not n:
        return jsonify({"error": 'Missing "n" parameter'}), 400

    return get_top_usage_api(int(n))


@views.route("/common-movesets", methods=["GET"])
def api_common_movesets():
    pokemon = request.args.get("pokemon")

    if not pokemon:
        return jsonify({"error": 'Missing "pokemon" parameter'}), 400

    return jsonify(
        {
            "pokemon": pokemon,
        }
    )
