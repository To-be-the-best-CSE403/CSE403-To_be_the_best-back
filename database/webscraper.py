import requests
from bs4 import BeautifulSoup
import mysql.connector as mysql
import json
import re


 
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
    url = "https://www.smogon.com/stats/"+date+"/gen9ou-1500.txt"
    
    local_filename = "usage_rate.txt"

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
            
def get_pokedex_file():
    url = "https://play.pokemonshowdown.com/data/pokedex.json"
    
    local_filename = "pokedex.json"
    
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)            
                
def get_pokemon_data_file(date):
    url = "https://www.smogon.com/stats/"+date+"/moveset/gen9ou-1500.txt"
    local_filename = "pokemon_data.txt"
    
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
    with open('usage_rate.txt') as f:
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
                
def get_pokemon_data(connection, index):
    select_query = '''
    SELECT * FROM pokedex WHERE PokemonID = %s;
    '''
    cursor = connection.cursor()
    cursor.execute(select_query, index)
    result = cursor.fetchall()
    cursor.close()
    return result

def delete_table(connection):
    delete_query = '''
    DROP TABLE IF EXISTS pokemon;
    '''
    cursor = connection.cursor()
    cursor.execute(delete_query)
    connection.commit()
    cursor.close()


db_connection = create_db_connection()



db_connection.close()




