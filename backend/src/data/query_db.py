import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

config = {
    "user": os.getenv("DATABASE_USER"),
    "password": os.getenv("DATABASE_PASSWORD"),
    "host": os.getenv("DATABASE_HOST"),
    "database": os.getenv("DATABASE_NAME"),
    "port": 20973,
    "raise_on_warnings": True,
}


def create_db_connection():
    db_connection = mysql.connector.connect(**config)
    print("MySQL database connection successful")
    return db_connection


def get_top_usage(top_n: int):
    db_connection = mysql.connector.connect(**config)
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM usage_rate LIMIT %s", (top_n,))

    top_usage = cursor.fetchall()
    cursor.close()
    return top_usage


# Example usage
if __name__ == "__main__":
    print(get_top_usage(10))
