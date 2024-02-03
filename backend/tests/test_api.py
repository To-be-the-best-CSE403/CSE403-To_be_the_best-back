import pytest
from api.index import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_api_example(client):
    # Send a GET request to the api endpoint
    response = client.get('/api/test/home')
    
    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that the response data is as expected
    assert response.data == b'Test API'

def test_api_teambuilder(client):
    # Send a GET request to the api test '/teambuilder' endpoint
    response = client.get('/api/test/teambuilder')
    
    # Check that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Check that the response data is as expected
    expected_data = [
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
    assert response.json == expected_data