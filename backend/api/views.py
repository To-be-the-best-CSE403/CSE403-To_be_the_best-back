from flask import Blueprint, request, jsonify
from src.api.teambuilder.teambuilder_api import get_team

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


@views.route("/usage-rate")
def api_usage_rate():
    return [
        {
            "name": "Pikachu",
            "usage": 0.5,
        },
        {
            "name": "Charizard",
            "usage": 0.5,
        },
    ]


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
