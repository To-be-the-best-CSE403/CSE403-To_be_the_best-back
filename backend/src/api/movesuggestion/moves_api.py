from flask import jsonify
# from .moves_algo import opponent_type
from .moves_algo import most_effective

TYPES = set()


def get_move(opptype: str):
    """
    API for getting an optimal move based on the opponent's type provided.

    :param opptype: The type of the opponent.
    :return: A JSON response containing the most effective move.
    """
    opptype = opptype.lower()

    if opptype not in TYPES:
        return (
            jsonify({"error": f"Invalid type given, type should be one of: {TYPES}"}),
            400,
        )

    optimal = most_effective(opptype)

    return jsonify(optimal)
