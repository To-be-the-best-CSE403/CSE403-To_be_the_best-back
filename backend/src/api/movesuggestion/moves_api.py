from flask import jsonify
import json
import mysql.connector as mysql
import os



TYPES = set(["normal", "fire", "water", "electric",
            "grass", "ice", "fighting", "poison",
            "ground", "flying", "psychic", "bug",
            "rock", "ghost", "dragon", "dark",
            "steel", "fairy"])

def _load_type_chart():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "type_chart.json")
    try:
        with open(file_path) as file:
            type_chart = json.load(file)
        return type_chart
    except FileNotFoundError:
        print("type_chart.json not found")
        return -1

# TODO: replace jsonify returns with standard values
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
    
    :return: The corresponding number for the strongest move or negative 1 on failure
    """
    type_chart = _load_type_chart()
    
    powers = [move1power, move2power, move3power, move4power]
    move_types = [move1type, move2type, move3type, move4type]
    move_types = [type.lower() for type in move_types]
    
    for i in range(4):
        if move_types[i] not in TYPES:
            print("move" + str(i) + "type is invalid")
            return -1
            
    for i in range(4):
        if powers[i] < 0:
            print("move" + str(i) + "power is negative")
            return -1
    
    connection = _create_db_connection()
    cursor = connection.cursor()
    
    query_types = "SELECT Type1, Type2 FROM pokedex WHERE Name = %s"
    
    cursor.execute(query_types, (pokemon_name,))
    row = cursor.fetchone()
    if not row:
        print("Query error for pokemon types")
        return -1
    
    type1 = row[0].lower()
    if (len(row) > 1):
        type2 = row[1].lower()
    
    cursor.execute(query_types, (enemy_name,))
    row = cursor.fetchone()
    if not row:
        print("Query error for pokemon types")
        return -1
    
    enemy_type1 = row[0].lower()
    if (len(row) > 1):
        enemy_type2 = row[1].lower()
    
    cursor.close()
    connection.close()
    
    pokemon_types = [type1, type2]
    enemy_types = [enemy_type1, enemy_type2]
    
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
                    break
                    
            damage = move_power * modifier
            if damage > max_damage:
                max_damage = damage
                strongest_move = move_number

        
    return strongest_move


def _create_db_connection():
    connection = None
    try:
        connection = mysql.connect(
            host='to-be-the-best-wahidyassine2003-5e76.a.aivencloud.com',         # Replace with your host name
            user='avnadmin',         # Replace with your username
            password='AVNS_LJgWj8F_NlTVYgi3yVy',     # Replace with your password
            port = 20973,
            database='to_be_the_best', # Replace with your database name
        )
        print("MySQL Database connection successful")
    except mysql.Error as err:
        print(f"Error: '{err}'")

    return connection

