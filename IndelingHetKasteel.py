from py_database.db_connection import create_connection, close_connection, database_path
from py_vensters.hoofd_venster import Hoofdvenster


def main():
    # Maak verbinding met de database
    conn = create_connection(database_path)

    # Voer hier eventuele databasebewerkingen uit, zoals het ophalen van gegevens of het bijwerken van tabellen

    # Open het hoofdvenster
    app = Hoofdvenster()
    app.mainloop()

    # Sluit de verbinding met de database
    close_connection(conn)


if __name__ == "__main__":
    main()
