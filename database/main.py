import pymysql

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="PokemonShowdown",
    host="mysql-36ad1e69-pokemon-showdown-database.a.aivencloud.com",
    password="AVNS_pk22TjyN_GsQdf9CP_o",
    read_timeout=timeout,
    port=14966,
    user="avnadmin",
    write_timeout=timeout,
)

try:
    cursor = connection.cursor()
#     cursor.execute(("CREATE TABLE pokemon ("
#                     "species varchar(255) NOT NULL,"
#                     "usage_rate DECIMAL(4, 2),"
#                     "moves varchar(1023),"
#                     "items varchar(1023),"
#                     "abilities varchar(1023),"
#                     "spreads varchar(1023),"
#                     "teammates varchar(1023),"
#                     "PRIMARY KEY (species)"
#                     ");"))
    sql_insert = ("INSERT INTO pokemon (species, usage_rate, moves, items, abilities, spreads, teammates)"
            " VALUES (%s, %s, %s, %s, %s, %s, %s)")
    species = "Kingambit"
    usage_rate = 0.37
    moves = ("Sucker Punch 99.680%\n"
            "Swords Dance 95.253%\n"
            "Kowtow Cleave 82.292%\n" 
            "Iron Head 70.318%\n"
            "Low Kick 32.923%\n"
            "Other 19.535%")
    items = ("Leftovers 39.651%\n"
            "Black Glasses 19.576%\n"
            "Air Balloon 19.525%\n"
            "Heavy-Duty Boots  8.696%\n" 
            "Lum Berry  8.694%\n"
            "Other  3.858%"
             )
    abilities = ("Supreme Overlord 99.457%\n"
            "Defiant  0.277%\n"
            "Pressure  0.266%"
             )
    spreads = ("Adamant:0/252/4/0/0/252 21.793%\n"
            "Adamant:0/252/0/0/4/252 12.426%\n"
            "Adamant:208/252/0/0/0/48  8.364%\n"
            "Jolly:0/252/4/0/0/252  7.529%\n" 
            "Adamant:216/252/0/0/0/40  5.404%\n"
            "Adamant:236/252/0/0/0/20  5.058%\n"
            "Other 39.427%"
             )
    teammates = ("Iron Boulder 28.523%\n"
            "Glimmora 27.665%\n"
            "Volcarona 27.160%\n"
            "Roaring Moon 24.736%\n" 
            "Hatterene 24.022%\n"
            "Great Tusk 19.819%\n"
            "Iron Valiant 16.569%\n"
            "Deoxys-Speed 15.867%\n"
            "Enamorus 15.025%\n"
            "Gouging Fire 14.917%\n"
            "Slowking-Galar 12.972%"
            )
    cursor.execute(sql_insert, (species, usage_rate, moves, items, abilities, spreads, teammates))
    cursor.execute("SELECT * FROM pokemon")
    rows = cursor.fetchall()
    print(rows)
finally:
    connection.close()
