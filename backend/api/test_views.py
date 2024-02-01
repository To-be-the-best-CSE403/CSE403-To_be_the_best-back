
from flask import Blueprint, request, jsonify

test_views = Blueprint('test_test_views', __name__)


@test_views.route('/home')
def api_index():
    return 'Test API'

@test_views.route('/teambuilder', methods=['GET'])
def api_teambuilder():
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
            "moves": ["Ice Beam", "Hurricane", "Substitute", "Roost"]
        },
        {
            "name": "",
            "species": "Ludicolo",
            "gender": "",
            "item": "Life Orb",
            "ability": "Swift Swim",
            "evs": {"hp": 4, "atk": 0, "def": 0, "spa": 252, "spd": 0, "spe": 252},
            "nature": "Modest",
            "moves": ["Surf", "Giga Drain", "Ice Beam", "Rain Dance"]
        },
        {
            "name": "",
            "species": "Volbeat",
            "gender": "M",
            "item": "Damp Rock",
            "ability": "Prankster",
            "evs": {"hp": 248, "atk": 0, "def": 252, "spa": 0, "spd": 8, "spe": 0},
            "nature": "Bold",
            "moves": ["Tail Glow", "Baton Pass", "Encore", "Rain Dance"]
        },
        {
            "name": "",
            "species": "Seismitoad",
            "gender": "",
            "item": "Life Orb",
            "ability": "Swift Swim",
            "evs": {"hp": 0, "atk": 0, "def": 0, "spa": 252, "spd": 4, "spe": 252},
            "nature": "Modest",
            "moves": ["Hydro Pump", "Earth Power", "Stealth Rock", "Rain Dance"]
        },
        {
            "name": "",
            "species": "Alomomola",
            "gender": "",
            "item": "Damp Rock",
            "ability": "Regenerator",
            "evs": {"hp": 252, "atk": 0, "def": 252, "spa": 0, "spd": 4, "spe": 0},
            "nature": "Bold",
            "moves": ["Wish", "Protect", "Toxic", "Rain Dance"]
        },
        {
            "name": "",
            "species": "Armaldo",
            "gender": "",
            "item": "Leftovers",
            "ability": "Swift Swim",
            "evs": {"hp": 128, "atk": 252, "def": 4, "spa": 0, "spd": 0, "spe": 124},
            "nature": "Adamant",
            "moves": ["X-Scissor", "Stone Edge", "Aqua Tail", "Rapid Spin"]
        }
    ]
