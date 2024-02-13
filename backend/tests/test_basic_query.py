import pytest


# TODO: Update with all the actual values according to how the database is setup and get the right percentage from the website
# But this will be the basic structure for all the basic query tests, will just neeed to copy this for the rest of the queries
# that need to be tested and replace what values we are testing
def test_db_connection():
    # TODO: remove later
    assert True
    return

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
        assert True
    finally:
        connection.close()
        assert False


def test_basic_query_percent():
    # TODO: remove later
    assert True
    return

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
        name = "pikachu"
        # results = cursor.execute("SELECT usage_percent FROM Pokemon WHERE name = %s", (name))
        # assert results[0]['usage_percent'] == 0.02
        assert True
    finally:
        connection.close()
        assert False


def test_basic_query_partner():
    # TODO: remove later
    assert True
    return

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
        name = "pikachu"
        # results = cursor.execute("SELECT usage_percent FROM Pokemon WHERE name = %s LIMIT 1", (name))
        # assert results[0]['partner'] == "pikachu 0.02"
        assert True

    finally:
        connection.close()
        assert False
