import random
import json
import os


def compute_team(archetype: str):
    """
    Returns a team based on the archetype provided.

    :param archetype: The archetype of the team to get.
    :return: the team which consists of a list of pokemon.
    """

    # For now we will return hardcoded teams
    try:
        path = os.path.join(
            "src", "api", "teambuilder", f"teambuilder_{archetype}.json"
        )
        with open(path) as file:
            return random.choice(json.load(file))
    except FileNotFoundError:
        return None
