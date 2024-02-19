from flask import Blueprint, request, jsonify
from src.constants import DEFAULT_DATE, DEFAULT_TIER, DEFAULT_BASELINE
from src.api.teambuilder.teambuilder_api import get_team
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
