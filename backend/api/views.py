from flask import Blueprint, request, jsonify
from src.api.teambuilder.teambuilder_api import get_team
from src.data.constants import DEFAULT_DATE, DEFAULT_TIER, DEFAULT_BASELINE
from src.data.query_json import get_top_usage
from src.data.query_json import get_timeline_usage

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
    API endpoint to get the top n Pokemon usage rates for a given date, tier, and baseline
    Example usage:
    /usage-rate?
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

    try:
        top_usage = get_top_usage(int(n), date, tier, int(baseline))
        return jsonify(top_usage)
    except FileNotFoundError:
        return jsonify({"error": f"No usage found for {date}, {tier}, {baseline}"}), 404


@views.route("/usage-timeline", methods=["GET"])
def api_usage_timeline():
    """
    API endpoint to get the usage rates for a given set of Pokemon over a specified duration starting from a given date
    Example usage:
    /usage-timeline?
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

    try:
        usage = get_timeline_usage(
            pokemons,
            start_date,
            int(duration),
            tier,
            int(baseline),
        )
        return jsonify(usage)
    except FileNotFoundError:
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
