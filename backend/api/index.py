from flask import Flask, request, jsonify
from flask_cors import CORS
from src.data.constants import DEFAULT_DATE, DEFAULT_TIER, DEFAULT_BASELINE
from src.data.query_json import get_top_usage
from src.data.query_json import get_timeline_usage
from src.api.teambuilder.teambuilder_api import get_team

app = Flask(__name__)
CORS(app)


@app.route("/api")
def api_home():
    return "Hello, World!"


@app.route("/api/teambuilder", methods=["GET"])
def api_teambuilder():
    archetype = request.args.get("archetype")
    if not archetype:
        return jsonify({"error": "Teambuilder archetype parameter is missing"}), 400

    return get_team(archetype)


@app.route("/api/usage-rate", methods=["GET"])
def api_usage_rate():
    """
    API endpoint to get the top n Pokemon usage rates for a given date, tier, and baseline
    Example usage:
    /api/usage-rate?
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


@app.route("/api/usage-timeline", methods=["GET"])
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


@app.route("/api/common-movesets", methods=["GET"])
def api_common_movesets():
    pokemon = request.args.get("pokemon")

    if not pokemon:
        return jsonify({"error": 'Missing "pokemon" parameter'}), 400

    return jsonify(
        {
            "pokemon": pokemon,
        }
    )


@app.route("/api/test/home")
def api_index():
    return "Test API"


@app.route("/api/test/teambuilder", methods=["GET"])
def api_test_teambuilder():
    return [
        {
            "name": "",
            "species": "Articuno",
            "gender": "",
            "item": "Leftovers",
            "ability": "Pressure",
            "evs": {"hp": 252, "atk": 0, "def": 0, "spa": 252, "spd": 4, "spe": 0},
            "nature": "Modest",
            "ivs": {"hp": 31, "atk": 31, "def": 31, "spa": 30, "spd": 30, "spe": 31},
            "moves": ["Ice Beam", "Hurricane", "Substitute", "Roost"],
        },
        {
            "name": "",
            "species": "Ludicolo",
            "gender": "",
            "item": "Life Orb",
            "ability": "Swift Swim",
            "evs": {"hp": 4, "atk": 0, "def": 0, "spa": 252, "spd": 0, "spe": 252},
            "nature": "Modest",
            "moves": ["Surf", "Giga Drain", "Ice Beam", "Rain Dance"],
        },
        {
            "name": "",
            "species": "Volbeat",
            "gender": "M",
            "item": "Damp Rock",
            "ability": "Prankster",
            "evs": {"hp": 248, "atk": 0, "def": 252, "spa": 0, "spd": 8, "spe": 0},
            "nature": "Bold",
            "moves": ["Tail Glow", "Baton Pass", "Encore", "Rain Dance"],
        },
        {
            "name": "",
            "species": "Seismitoad",
            "gender": "",
            "item": "Life Orb",
            "ability": "Swift Swim",
            "evs": {"hp": 0, "atk": 0, "def": 0, "spa": 252, "spd": 4, "spe": 252},
            "nature": "Modest",
            "moves": ["Hydro Pump", "Earth Power", "Stealth Rock", "Rain Dance"],
        },
        {
            "name": "",
            "species": "Alomomola",
            "gender": "",
            "item": "Damp Rock",
            "ability": "Regenerator",
            "evs": {"hp": 252, "atk": 0, "def": 252, "spa": 0, "spd": 4, "spe": 0},
            "nature": "Bold",
            "moves": ["Wish", "Protect", "Toxic", "Rain Dance"],
        },
        {
            "name": "",
            "species": "Armaldo",
            "gender": "",
            "item": "Leftovers",
            "ability": "Swift Swim",
            "evs": {"hp": 128, "atk": 252, "def": 4, "spa": 0, "spd": 0, "spe": 124},
            "nature": "Adamant",
            "moves": ["X-Scissor", "Stone Edge", "Aqua Tail", "Rapid Spin"],
        },
    ]
