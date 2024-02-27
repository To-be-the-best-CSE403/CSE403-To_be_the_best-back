import json
import os

def optimal_moveset(pokemon: str):
    """
    API for getting an optimal moveset based on the Pokemon provided.

    :param pokemon: The pokemon that the user wants a moveset from.
    :return: A JSON response containing the moveset.
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
