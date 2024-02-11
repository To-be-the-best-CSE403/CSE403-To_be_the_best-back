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
        path = os.path.join(
            "src", "api", "movesuggestion", f"teambuilder_{moves}.json"
        )
        with open(path) as file:
            return json.load(file)
    except FileNotFoundError:
        return None
