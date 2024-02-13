import requests
from bs4 import BeautifulSoup
import mysql.connector as mysql
import json
import re
import ast

 
def create_db_connection():
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

def get_usage_file(date):
    url = "https://www.smogon.com/stats/{date}/gen9ou-1500.txt"
    
    local_filename = r"CSE403-To_be_the_best-back\database\pokedex_rate.txt"

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
            
def get_pokedex_file():
    url = "https://play.pokemonshowdown.com/data/pokedex.json"
    
    local_filename = r"CSE403-To_be_the_best-back\database\pokedex.json"
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)            
                
def get_pokemon_data_file(date):
    url = "https://www.smogon.com/stats/"+date+"/moveset/gen9ou-1500.txt"
    local_filename = r"CSE403-To_be_the_best-back\database\pokemon_data.txt"
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
def create_table_pokedex(connection):
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS pokedex (
            PokemonID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(100),
            Type1 VARCHAR(50),
            Type2 VARCHAR(50) NULL,
            HP INT,
            Atk INT,
            Def INT,
            Spa INT,
            Spd INT,
            Spe INT,
            Ability1 VARCHAR(100),
            AbilityHidden VARCHAR(100),
            Tier VARCHAR(50)
        );
    '''
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    
def create_table_pokemons(connection):
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS pokemon (
            PokemonID INT AUTO_INCREMENT PRIMARY KEY,
            name varchar(255),
            moves varchar(2048),
            items varchar(1023),
            abilities varchar(1023),
            spreads varchar(1023),
            teammates varchar(1023)
        );
    '''
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

def create_table_usage(connection):
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS usage_rate (
            PokemonID INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            usage_rate DECIMAL(7, 5)
        );
    '''
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()

 
def insert_data_pokedex(connection, data):
    insert_query = '''
    INSERT INTO pokedex (Name, Type1, Type2, HP, Atk, Def, Spa, Spd, Spe, Ability1, AbilityHidden, Tier)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    '''
    cursor = connection.cursor()
    cursor.execute(insert_query, data)
    connection.commit()
    cursor.close()

def insert_data_pokemons(connection, data):
    insert_query = '''
    INSERT INTO pokemon (name, moves, items, abilities, spreads, teammates)
    VALUES (%s, %s, %s, %s, %s, %s);
    '''
    cursor = connection.cursor()
    cursor.execute(insert_query, data)
    connection.commit()
    cursor.close() 
    
def insert_data_usage(connection, data):
    insert_query = '''
    INSERT INTO usage_rate (name, usage_rate)
    VALUES (%s, %s);
    '''
    cursor = connection.cursor()
    cursor.execute(insert_query, data)
    connection.commit()
    cursor.close()

 
def populate_pokedex(connection):
    with open('pokedex.json') as json_file:
        pokedex = json.load(json_file)
        for pokemon in pokedex.values():
            name = pokemon['name']
            types = pokemon["types"] + [""] * (2 - len(pokemon["types"]))
            base_stats = pokemon['baseStats']
            abilities = [pokemon['abilities'].get(str(i), None) for i in range(2)] + [pokemon["abilities"].get("H", None)]
            tier = pokemon.get("tier", None)
            data = (name,
                        types[0],
                        types[1],
                        base_stats["hp"],
                        base_stats["atk"],
                        base_stats["def"],
                        base_stats["spa"],
                        base_stats["spd"],
                        base_stats["spe"],
                        abilities[0],
                        abilities[-1],
                        tier,
                    )
            insert_data_pokedex(db_connection, data)
                
def populate_usage(connection):
    with open('pokedex_rate.txt') as f:
        for line in f:
            if line[1] == "|":
                line = line.split("|")
                name = line[2].strip()
                usage_rate = line[3].strip().strip("%")
                insert_data_usage(connection, (name, usage_rate))
                
def populate_pokemons(connection):
    with open("pokemon_data.txt", "r") as f:
        content = f.read()
        
    pokemons_data = re.split(r'\+\-+\+\s*\+\-+\+', content)
    
    for pokemon in pokemons_data:
        section = pokemon.split("+----------------------------------------+")
        name = section[0].replace("|", "").strip()
        abilities = section[2].replace("|", "").strip().split("\n")
        abilities = [ability.split() for ability in abilities]
        abilities.pop(0)
        abilities = [(" ".join(ability[:-1]), float(ability[-1].rstrip("%")) ) for ability in abilities]
        items = section[3].replace("|", "").strip().split("\n")
        items = [item.split() for item in items]
        items.pop(0)
        items = [(" ".join(item[:-1]), float(item[-1].rstrip("%")) ) for item in items]
        spreads = section[4].replace("|", "").strip().split("\n")
        spreads = [spread.split() for spread in spreads]
        spreads.pop(0)
        spreads = [(" ".join(spread[:-1]), float(spread[-1].rstrip("%")) ) for spread in spreads]
        moves = section[5].replace("|", "").strip().split("\n")
        moves = [move.split() for move in moves]
        moves.pop(0)
        moves = [(" ".join(move[:-1]), float(move[-1].rstrip("%")) ) for move in moves]
        teammates = section[6].replace("|", "").strip().split("\n")
        teammates = [teammate.split() for teammate in teammates]
        teammates.pop(0)
        teammates = [(" ".join(teammate[:-1]), float(teammate[-1].rstrip("%")) ) for teammate in teammates] 
        
        data = (name, str(moves), str(items), str(abilities), str(spreads), str(teammates))
        insert_data_pokemons(connection, data)

def delete_table(connection, table_name):
    delete_query = f'''
    DROP TABLE IF EXISTS {table_name};
    '''
    cursor = connection.cursor()
    cursor.execute(delete_query)
    connection.commit()
    cursor.close()

def reset_database():
    db_connection = create_db_connection()

    get_pokemon_data_file("2024-01")
    get_pokedex_file()
    get_usage_file("2024-01")

    delete_table(db_connection, "pokedex")
    delete_table(db_connection, "pokemon")
    delete_table(db_connection, "usage_rate")

    create_table_pokedex(db_connection)
    create_table_pokemons(db_connection)
    create_table_usage(db_connection)

    populate_pokedex(db_connection)
    populate_usage(db_connection)
    populate_pokemons(db_connection)

    db_connection.close()


def get_pokemon_data(connection, n = 6):
    
    pokemons = {}
    
    get_most_used_pokemon_query = '''
        SELECT * FROM usage_rate ORDER BY usage_rate DESC LIMIT %s;
    '''
    cursor = connection.cursor()
    cursor.execute(get_most_used_pokemon_query, (n,))
    result_1 = cursor.fetchall()
    
    for pokemon in result_1:
        name = pokemon[1]
        
        get_pokemon_data_query = '''
            SELECT * FROM pokemon WHERE name = %s;
        '''
        cursor.execute(get_pokemon_data_query, (name,))
        result_2 = cursor.fetchall()
        
        name, moves, items, abilities, spreads, teammates = translate_data(result_2[0])
        
        pokemons[name] = {"species": name, "usage_rate": float(pokemon[2]), "moves": moves, "items": items, "abilities": abilities, "spreads": spreads, "teammates": teammates}
        
    
    cursor.close()
    return pokemons

def translate_data(data):
    
    name = data[1]
    moves_dict = {}
    for move in ast.literal_eval(data[2]):
        moves_dict[move[0]] = move[1]
    items_dict = {}
    for item in ast.literal_eval(data[3]):
        items_dict[item[0]] = item[1]
        items_dict.pop("Other", None)
    abilities_dict = {}
    for ability in ast.literal_eval(data[4]):
        abilities_dict[ability[0]] = ability[1]
        abilities_dict.pop("Other", None)
    spreads_dict = {}
    for spread in ast.literal_eval(data[5]):
        s = spread[0].split(":")
        nature = s[0]
        evs = s[1] if len(s) > 1 else "0/0/0/0/0/0"
        hp, atk, def_, spa, spd, spe = evs.split("/")
        spreads_dict[nature] = (spread[1], {"hp": int(hp), "atk": int(atk), "def": int(def_), "spa": int(spa), "spd": int(spd), "spe": int(spe)})
        spreads_dict.pop("Other", None)
    teammates_dict = {}
    for teammate in ast.literal_eval(data[6]):
        teammates_dict[teammate[0]] = teammate[1]
        spreads_dict.pop("Other", None)
    
    return name, moves_dict, items_dict, abilities_dict, spreads_dict, teammates_dict
    
def create_team(pokemons, team_name):
    team = []
    for pokemon in pokemons.values():
        slot = {}
    
        slot["name"] = ""
        slot["species"] = pokemon["species"]
        slot["gender"] = ""
        slot["item"] = max(pokemon["items"], key=pokemon["items"].get) 
        slot["ability"] = max(pokemon["abilities"], key=pokemon["abilities"].get)
        best_spread = max(pokemon["spreads"], key= lambda k :pokemon["spreads"][k][0])
        slot["evs"] = pokemon["spreads"][best_spread][1]
        slot["nature"] = best_spread
        slot["moves"] = sorted(pokemon["moves"], key=pokemon["moves"].get, reverse=True)[:4]
        
        team.append(slot)
        
    with open(r"CSE403-To_be_the_best-back\backend\src\api\teambuilder\web_scraper_"+ team_name + ".json", "w") as f:
        json.dump(team, f)
    
    return team


pokemons = get_pokemon_data(create_db_connection())
create_team = create_team(pokemons, "team_1")




