import mysql.connector as mysql


INFO_TYPES = set(["moves", "items", "abilities", "spreads", "teammates"])

def retrieve_info(pokemon: str, info_type: str):
    info_type = info_type.lower()
    pokemon = pokemon.lower()

    if info_type not in INFO_TYPES:
        return ""

    query = f"SELECT {info_type} FROM pokemon WHERE name = %s"

    connection = _create_db_connection()
    cursor = connection.cursor()

    cursor.execute(query, (pokemon,))

    row = cursor.fetchone()

    if not row:
        print("Query error for pokemon info retrieval")
        return ""

    info = row[0].lower()

    cursor.close()
    connection.close()
    print("initial:\n" + info)

    # Convert the string representation of list to an actual list of tuples
    data_list = eval(info)

    formatted_output = ""
    for move, percent in data_list:
        formatted_output += f"{move}: {percent}%\n"

    formatted_output = formatted_output.strip()  # Remove any leading/trailing whitespace

    return formatted_output.title()


def _create_db_connection():
    connection = None
    try:
        connection = mysql.connect(
            host='to-be-the-best-wahidyassine2003-5e76.a.aivencloud.com',
            user='avnadmin',
            password='AVNS_LJgWj8F_NlTVYgi3yVy',
            port=20973,
            database='to_be_the_best',
        )
        print("MySQL Database connection successful")
    except mysql.Error as err:
        print(f"Error: '{err}'")

    return connection