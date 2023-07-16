import csv
import random
import os
def inlezen_spelers(hoofdvenster):
    try:
        with open('py_database/spelers.txt', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                achternaam, voornaam, elo, groep = row
                # Je kunt de ingelezen waarden nu verder verwerken
                # Bijvoorbeeld, print ze naar het output venster:
                hoofdvenster.print_to_output(
                    f"Achternaam: {achternaam}, Voornaam: {voornaam}, Elo: {elo}, Groep: {groep}")
    except Exception as e:
        hoofdvenster.print_to_output(f"Er is een fout opgetreden bij het inlezen van de spelers: {str(e)}")

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
    hoofdvenster.print_to_output("Toernooi Informatie knop is geklikt, implementeer de functie hier")

def aanwezigheid_spelers(hoofdvenster):
    # Implementeer de functie om de aanwezigheid van spelers te registreren
    hoofdvenster.print_to_output("Aanwezigheid Spelers knop is geklikt, implementeer de functie hier")

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
    # Implementeer de functie om het programma af te sluiten
    hoofdvenster.print_to_output("Afsluiten knop is geklikt, implementeer de functie hier")