from flask import Blueprint, request, jsonify
from src.constants import DEFAULT_DATE, DEFAULT_TIER, DEFAULT_BASELINE
from src.api.teambuilder.teambuilder_api import get_team
from database.webscraper import get_data_specific
from src.api.movesuggestion.moves_api import compute_effectiveness
from src.api.endpoints import get_usage_rate, get_usage_top, get_usage_timeline

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


@views.route("/usage-rate", methods=["GET"])
def api_usage_rate():
    """
    API endpoint to get the usage rate for a given Pokemon, date, tier, and baseline
    Example usage:
    /api/usage-rate?
    pokemon=GreatTusk
    """
    pokemon = request.args.get("pokemon")
    if not pokemon:
        return jsonify({"error": 'Missing "pokemon" parameter'}), 400

    date = request.args.get("date", DEFAULT_DATE)
    tier = request.args.get("tier", DEFAULT_TIER)
    baseline = request.args.get("baseline", DEFAULT_BASELINE)

    usage_rate = get_usage_rate(pokemon, date, tier, int(baseline))
    if usage_rate:
        return jsonify(usage_rate)
    else:
        return (
            jsonify({"error": f"No usage found for {pokemon}, {date}, {tier}"}),
            404,
        )


@views.route("/usage-top", methods=["GET"])
def api_usage_top():
    """
    API endpoint to get the top n Pokemon usage rates for a given date, tier, and baseline
    Example usage:
    /api/usage-top?
    n=10&
    date=2023-01&
    tier=gen9ou&
    baseline=1500
    """
    n = request.args.get("n")
    if not n:
        return jsonify({"error": 'Missing "n" parameter'}), 400

    date = request.args.get("date", DEFAULT_DATE)
    tier = request.args.get("tier", DEFAULT_TIER)
    baseline = request.args.get("baseline", DEFAULT_BASELINE)

    top_usage = get_usage_top(int(n), date, tier, int(baseline))
    if top_usage:
        return jsonify(top_usage)
    else:
        return jsonify({"error": f"No usage found for {date}, {tier}, {baseline}"}), 404


@views.route("/usage-timeline", methods=["GET"])
def api_usage_timeline():
    """
    API endpoint to get the usage rates for a given set of Pokemon over a specified duration starting from a given date
    Example usage:
    /api/usage-timeline?
    pokemons=GreatTusk&
    pokemons=Kingambit&
    start_date=2023-01&
    duration=6
    """
    pokemons = request.args.getlist("pokemons")
    start_date = request.args.get("start_date")
    duration = request.args.get("duration", 1)
    tier = request.args.get("tier", DEFAULT_TIER)
    baseline = request.args.get("baseline", DEFAULT_BASELINE)

    if not pokemons:
        return jsonify({"error": 'Missing "pokemons" parameter'}), 400
    if not start_date:
        return jsonify({"error": 'Missing "start_date" parameter'}), 400

    usage_timeline = get_usage_timeline(
        pokemons, start_date, int(duration), tier, int(baseline)
    )
    if usage_timeline:
        return jsonify(usage_timeline)
    else:
        return (
            jsonify({"error": f"No usage found for {start_date}, {duration}, {tier}"}),
            404,
        )


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
