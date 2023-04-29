from py_vensters.hoofd_venster import toon_spelers
from py_vensters.hoofd_venster import maak_venster
from py_lijsten.lijsten import spelers


def inlezen_spelers():
    # Maak de spelersA lijst leeg
    spelers.clear()

    # Open het tekstbestand in leesmodus
    with open("txt_databases/spelers.txt", "r") as file:
        for line in file:
            # Verwijder witruimte en splits de regel op komma's
            naam, voornaam, elo = line.strip().split(',')

            # Converteer de elo naar een integer
            elo = int(elo)

            # Voeg de naam, voornaam en elo toe aan de spelersA lijst
            spelers.append((naam, voornaam, elo))

    # Sorteer de spelersA lijst op Elo, van hoog naar laag
    spelers.sort(key=lambda speler: speler[2], reverse=True)

    # Ken een nummer toe aan elke speler
    genummerde_spelers = [(index + 1, *speler) for index, speler in enumerate(spelers)]

    # Toon de namen van de spelers in een afzonderlijk venster
    toon_spelers(genummerde_spelers)


def main():
    # Maak een venster met de benodigde knoppen
    root, inlezen_spelers_button = maak_venster()

    # Koppel de functie 'inlezen_spelers' aan de knop 'inlezen_spelers_button'
    inlezen_spelers_button.config(command=inlezen_spelers)

    # Start de tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()