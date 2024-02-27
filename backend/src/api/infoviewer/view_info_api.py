import mysql.connector as mysql


INFO_TYPES = set(["moves", "items", "abilities",
                  "spreads", "teammates"])

# TODO: work on how to format the return value
def retrieve_info(pokemon: str, info_type: str):
    info_type = info_type.lower()
    pokemon = pokemon.lower()
    
    if info_type not in INFO_TYPES:
        return ""
    
    query = "SELECT %s FROM pokemon WHERE name = %s"
    
    connection = _create_db_connection()
    cursor = connection.cursor()
    
    cursor.execute(query, (info_type, pokemon))
    
    row = cursor.fetchone()
    
    if not row:
        print("Query error for pokemon info retrieval")
        return ""
    
    info = row[0].lower()
    
    cursor.close()
    connection.close()
    
    return info


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
