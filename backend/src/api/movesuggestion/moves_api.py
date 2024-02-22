from flask import jsonify
# from .moves_algo import opponent_type
from .moves_algo import most_effective
import json
from database.webscraper import create_db_connection

TYPES = set("normal", "fire", "water", "electric",
            "grass", "ice", "fighting", "poison",
            "ground", "flying", "psychic", "bug",
            "rock", "ghost", "dragon", "dark",
            "steel", "fairy")


def compute_effectiveness(move1type: str, move1power: int,
                          move2type: str, move2power: int,
                          move3type: str, move3power: int,
                          move4type: str, move4power: int,
                          pokemon_name: str, enemy_name: str):
    """
    Computes and returns the most effective moves based on the parameters
    
    :param move1type: Type of the first move
    :param move1power: Base power of the first move
    :param move2type: Type of the second move
    :param move2power: Base power of the second move
    :param move3type: Type of the third move
    :param move3power: Base power of the third move
    :param move4type: Type of the fourth move
    :param move4power: Base power of the fourth move
    :param pokemon_name: Name of user pokemon
    :param enemy_name: enemy pokemon name
    
    :return: The corresponding number for the strongest move
    """
    with open("type_chart.json", "r") as json_file:
        type_chart = json.load(json_file)
    
    move1type.lower()
    move2type.lower()
    move3type.lower()
    move4type.lower()
    
    if move1type not in TYPES:
        return (
            jsonify({"error": "move1type is invalid"})
        )
    if move2type not in TYPES:
        return (
            jsonify({"error": "move2type is invalid"})
        )    
    if move3type not in TYPES:
        return (
            jsonify({"error": "move3type is invalid"})
        )    
    if move4type not in TYPES:
        return (
            jsonify({"error": "move4type is invalid"})
        )
        
    connection = create_db_connection()
    cursor = connection.cursor()
    
    query_types = "SELECT Type1, Type2 FROM pokedex WHERE Name = %s"
    
    cursor.execute(query_types, (pokemon_name))
    row = cursor.fetchone()
    if not row:
        return (
            jsonify({"error": "Query error for pokemon types"})
        )
    type1 = row[0].lower()
    if (len(row) > 1):
        type2 = row[1].lower()
    
    cursor.execute(query_types, (enemy_name))
    row = cursor.fetchone()
    if not row:
        return (
            jsonify({"error": "Query error for pokemon types"})
        )
    enemy_type1 = row[0].lower()
    if (len(row) > 1):
        enemy_type2 = row[1].lower()
    
    cursor.close()
    connection.close()
    
    powers = [move1power, move2power, move3power, move4power]
    pokemon_types = [type1, type2]
    enemy_types = [enemy_type1, enemy_type2]
    move_types = [move1type, move2type, move3type, move4type]
    
    max_damage = 0
    strongest_move = None
    
    for move_number, (move_type, move_power) in enumerate(zip(move_types, powers), start=1):
        if move_power > 0:
            modifier = 1.0
            for enemy_type in enemy_types:
                if enemy_type:
                    modifier *= type_chart[move_type][enemy_type]
            for pokemon_type in pokemon_types:
                if pokemon_type == move_type:
                    modifier *= 1.5
                    
            damage = move_power * modifier
            if damage > max_damage:
                max_damage = damage
                strongest_move = move_number

        
    return jsonify({"move_number": strongest_move})

