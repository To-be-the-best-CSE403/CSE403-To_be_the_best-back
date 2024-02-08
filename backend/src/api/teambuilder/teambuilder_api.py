from flask import jsonify
from .teambuilder_algo import compute_team

ARCHETYPES = set(["ho", "bo", "stall", "balance", "weather"])


def get_team(archetype: str):
    """
    API for getting a team based on the archetype provided.

    :param archetype: The archetype of the team to get.
    :return: A JSON response containing the team.
    """
    archetype = archetype.lower()

    if archetype not in ARCHETYPES:
        return (
            jsonify({"error": f"Invalid archetype should be one of: {ARCHETYPES}"}),
            400,
        )

    team = compute_team(archetype)

    if not team or len(team) == 0 or len(team) > 6:
        return jsonify({"error": f"No team found for archetype: {archetype}"}), 404

    return jsonify(team)
