from flask import Blueprint, request, jsonify
from src.api.teambuilder.teambuilder_api import get_team
from database.webscraper import get_data_specific
from src.api.movesuggestion.moves_api import compute_effectiveness

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

#TODO: figure out how to properly handle the variable number url
@views.route("/battle-gen9ou-<int:battleid>", methods=["GET"])
def move_selector(battleid: int):
    move1type = request.args.get("move1type")
    move2type = request.args.get("move2type")
    move3type = request.args.get("move3type")
    move4type = request.args.get("move4type")
    
    move1power = int(request.args.get("move1power"))
    move2power = int(request.args.get("move2power"))
    move3power = int(request.args.get("move3power"))
    move4power = int(request.args.get("move4power"))
    
    pokemon_name = request.args.get("pokemon_name")
    enemy_name = request.args.get("enemy_name")
    
    if not move1type or move2type or move3type or move4type:
        return jsonify(
            {"error": "A move type parameter is missing for move selector"}), 400
    
    if not move1power or move2power or move3power or move4power:
        return jsonify(
            {"error": "A move power parameter is missing for move selector"}), 400
    if not pokemon_name:
        return jsonify(
            {"error": "pokemon_name parameter is missing for move selector"}), 400
    if not enemy_name:
        return jsonify(
            {"error": "enemy_name parameter is missing for move selector"}), 400

    return compute_effectiveness(move1type, move1power,
                                 move2type, move2power,
                                 move3type, move3power,
                                 move4type, move4power,
                                 pokemon_name, enemy_name)


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
