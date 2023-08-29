import os
import sqlite3
from sqlite3 import Error
import shutil
import datetime

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

def clear_spelers_table(conn):
    """Clear the spelers table by deleting all its rows."""
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM spelers")
        conn.commit()
    except sqlite3.Error as error:
        print("Failed to clear the spelers table:", error)

def get_all_spelers(conn):
    """Fetch all players from the spelers table."""
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM spelers")
        return cursor.fetchall()
    except sqlite3.Error as error:
        print("Failed to fetch players from the spelers table:", error)
        return []

def get_informatie(conn):
    """Haal de informatie op van de tabel 'informatie'."""
    cursor = conn.cursor()
    cursor.execute("SELECT seizoen, periode, ronde FROM informatie")
    result = cursor.fetchone()
    return result


def save_informatie(conn, seizoen, periode, ronde):
    """Save the tournament information to the database."""

    cursor = conn.cursor()

    # Check if there's already a record in the informatie table
    cursor.execute("SELECT COUNT(*) FROM informatie")
    count = cursor.fetchone()[0]

    if count == 0:
        # If no record, insert the information
        cursor.execute("INSERT INTO informatie (seizoen, periode, ronde) VALUES (?, ?, ?)", (seizoen, periode, ronde))
    else:
        # If there's a record, update the information
        cursor.execute("UPDATE informatie SET seizoen = ?, periode = ?, ronde = ?", (seizoen, periode, ronde))

    conn.commit()

def verwijderen_tabellen(conn):

    cursor = conn.cursor()

    # Vraag de namen van alle tabellen in de database op
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Verwijder elke tabel
    for table in tables:
        cursor.execute(f"DROP TABLE {table[0]}")

    # Sluit de verbinding
    conn.close()

def backup_database(database_path, backup_folder=None):
    """Create a backup of the SQLite3 database.

    Parameters:
    - database_path (str): Path to the SQLite3 database file.
    - backup_folder (str, optional): Directory where the backup should be saved. If None, the backup will be saved in the same directory as the database.

    Returns:
    - str: Path to the backup file or None if the backup failed.
    """
    try:
        if backup_folder is None:
            backup_folder = os.path.dirname(database_path)

        # Create the backup folder if it doesn't exist.
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        # Create the backup filename with a timestamp.
        current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f"backup_{current_time}.sqlite3"
        backup_path = os.path.join(backup_folder, backup_filename)

        # Copy the database file to the backup location.
        shutil.copy2(database_path, backup_path)

        print(f"Database backup successful: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"Error creating backup: {e}")
        return None


def restore_backup(database_path, backup_folder=None):
    """Restore the most recent SQLite3 database backup.

    Parameters:
    - database_path (str): Path where the restored database should be saved.
    - backup_folder (str, optional): Directory where the backups are saved. If None, it will assume the backups are in the same directory as the database.

    Returns:
    - bool: True if the restoration was successful, False otherwise.
    """
    try:
        if backup_folder is None:
            backup_folder = os.path.dirname(database_path)

        # Get list of all backup files in the backup folder
        backup_files = [f for f in os.listdir(backup_folder) if f.startswith("backup_") and f.endswith(".sqlite3")]

        # If there are no backup files, return False
        if not backup_files:
            print(f"No backups found in: {backup_folder}")
            return False

        # Sort the backup files to get the most recent backup
        latest_backup = sorted(backup_files, reverse=True)[0]
        latest_backup_path = os.path.join(backup_folder, latest_backup)

        # Restore the latest backup
        return restore_backup(latest_backup_path, database_path)
    except Exception as e:
        print(f"Error restoring latest backup: {e}")
        return False

def leegmaken_tabel(conn):
    """Empty all tables in the database without dropping them."""
    cursor = conn.cursor()

    # Fetch the names of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Begin a transaction
    conn.execute("BEGIN TRANSACTION;")
    try:
        # Empty each table
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DELETE FROM `{table_name}`;")

        # Commit the transaction
        conn.commit()
    except sqlite3.Error as error:
        # If any error occurs, rollback the transaction
        conn.rollback()
        print(f"Error emptying tables: {error}")