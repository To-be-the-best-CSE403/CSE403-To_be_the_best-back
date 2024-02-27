from flask import jsonify
import json
import os

def optimal_moveset(pokemon: str):
    """
    API for getting a team based on the archetype provided.

    :param archetype: The archetype of the team to get.
    :return: A JSON response containing the team.
    """
    pokemon = pokemon.lower().replace(" ", "")

    try:
        path = os.path.join(
            "src", "api", "moveset", f"moveset_{pokemon}.json"
        )
        with open(path) as file:
            return json.load(file)
    except FileNotFoundError:
        return None
