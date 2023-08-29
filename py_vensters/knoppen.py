import csv
import os
import random
from py_database.db_connection import clear_spelers_table
def inlezen_spelers(hoofdvenster, conn):
    try:
        # conn is passed as a parameter now
        cursor = conn.cursor()

        # Clear the spelers table
        clear_spelers_table(conn)

        with open('py_database/spelers.txt', 'r') as file:
            reader = csv.reader(file)
            nummer = 1
            for row in reader:
                achternaam, voornaam, elo, groep = row

                # Voeg de spelerinformatie toe aan de database
                hoofdvenster.print_to_output(f"Speler ingelezen: {voornaam.strip()} {achternaam.strip()} - Elo: {elo.strip()} - Groep: {groep.strip()}")
                cursor.execute("INSERT INTO spelers (nummer, achternaam, voornaam, elo, groep) VALUES (?, ?, ?, ?, ?)",(int(nummer), achternaam.strip(), voornaam.strip(), int(elo.strip()), groep.strip()))
                nummer += 1

        # Commit de wijzigingen
        conn.commit()

        hoofdvenster.print_to_output(
            "Spelersinformatie succesvol ingelezen vanuit py_database/spelers.txt en toegevoegd aan de database")

    except Exception as e:
        hoofdvenster.print_to_output(
            f"Er is een fout opgetreden bij het inlezen van de spelersinformatie en het toevoegen aan de database: {str(e)}")

    # finally:
        # Sluit de verbinding met de database
        # conn.close()  # Keeping the connection open

def uitlezen_spelers(hoofdvenster):
    try:
        # Maak de map aan als deze nog niet bestaat
        os.makedirs('py_database', exist_ok=True)

        with open('py_database/spelersuit.txt', 'w') as file:
            for _ in range(20):
                voornaam = f"Voornaam{_}"
                achternaam = f"Achternaam{_}"
                elo = random.randint(1000, 2800)  # Genereer een willekeurige ELO-rating tussen 1000 en 2800
                groep = random.choice(['A', 'B', 'C', 'D'])  # Kies willekeurig een groep uit de lijst ['A', 'B', 'C', 'D']

                # Schrijf de spelerinformatie naar het bestand zonder labels
                file.write(f"{achternaam}, {voornaam}, {elo}, {groep}\n")

            hoofdvenster.print_to_output("Spelersinformatie succesvol weggeschreven naar py_database/spelersuit.txt")
    except Exception as e:
        hoofdvenster.print_to_output(f"Er is een fout opgetreden bij het wegschrijven van de spelersinformatie: {str(e)}")

def toernooi_informatie(hoofdvenster):
    # Implementeer de functie om de toernooi informatie te tonen
    hoofdvenster.setup_informatie_tab()

def aanwezigheid_spelers(hoofdvenster):
    """Fetch all players from the database and display them in the Aanwezige spelers tab."""
    hoofdvenster.display_spelers_in_tab()

def indelen_ronde(hoofdvenster):
    # Implementeer de functie om de ronde in te delen
    hoofdvenster.print_to_output("Indelen Ronde knop is geklikt, implementeer de functie hier")
def verwijderen_ronde(hoofdvenster):
    # Implementeer de functie om de ronde te verwijderen
    hoofdvenster.print_to_output("Verwijderen Ronde knop is geklikt, implementeer de functie hier")

def uitslagen_ronde(hoofdvenster):
    # Implementeer de functie om de uitslagen van de ronde te registreren
    hoofdvenster.print_to_output("Uitslagen Ronde knop is geklikt, implementeer de functie hier")
def ranglijst(hoofdvenster):
    # Implementeer de functie om de ranglijst te tonen
    hoofdvenster.print_to_output("Ranglijst knop is geklikt, implementeer de functie hier")
def opslaan(hoofdvenster):
    # Implementeer de functie om de gegevens op te slaan
    hoofdvenster.print_to_output("Opslaan knop is geklikt, implementeer de functie hier")
def afsluiten(hoofdvenster):
    hoofdvenster.conn.close()
    hoofdvenster.destroy()
