import json
import os

def most_effective(type: str):
    """
    Returns a move based on the archetype provided.

    :param type: The type of the opponent.
    :return: the move / type of move that is the most effective.
    """

    # For now we will return hardcoded moves
    try:
        path = os.path.join("src", "api", "movesuggestion", f"moves_{type}.json")
        with open(path) as file:
            data = json.load(file)
            return data.get("moves_effective")  # Extract the moves_effective list from the JSON data
    except FileNotFoundError:
        return None
