import os
import sqlite3
from sqlite3 import Error

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(BASE_DIR, "IndelingHetKasteel.sqlite3")


def create_connection(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        print(f"sqlite3 version: {sqlite3.version}")
        print(f"Connection to database successful: {db_path}")
    except Error as e:
        print(e)

    return conn


def close_connection(conn):
    if conn:
        conn.close()
        print("Connection closed.")


if __name__ == "__main__":
    # Test the connection
    connection = create_connection(database_path)
    close_connection(connection)
