from py_database.db_connection import create_connection, close_connection, database_path
from py_vensters.hoofd_venster import Hoofdvenster


def main():
    # Maak verbinding met de database
    conn = create_connection(database_path)

    # Open het hoofdvenster
    app = Hoofdvenster(conn)
    app.mainloop()

    # Sluit de verbinding met de database
    close_connection(conn)


if __name__ == "__main__":
    main()

# Nog te doen:
# Bij inlezen spelers per speler checken of deze al een keer vrij is geweest.
# Bij het veranderen van de combox in het tabblad "Aanwezige Spelers" deze wijziging ook doorvoeren in de database.