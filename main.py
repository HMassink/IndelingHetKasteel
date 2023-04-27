import venster
from venster import toon_spelers

spelersA = []  # Lijst voor spelers in groep A
spelersBC = []  # Lijst voor spelers in groep BC

def inlezen_groep_A():
    # Maak de spelersA lijst leeg
    spelersA.clear()

    # Open het tekstbestand in leesmodus
    with open("spelersA.txt", "r") as file:
        for line in file:
            # Verwijder witruimte en splits de regel op komma's
            naam, voornaam, elo = line.strip().split(',')

            # Converteer de elo naar een integer
            elo = int(elo)

            # Voeg de naam, voornaam en elo toe aan de spelersA lijst
            spelersA.append((naam, voornaam, elo))

    # Sorteer de spelersA lijst op alfabetische volgorde van de achternaam
    spelersA.sort(key=lambda speler: speler[0])

    # Toon de namen van de spelers in een afzonderlijk venster
    toon_spelers(spelersA)

def main():
    root, inlezen_A_button, inlezen_BC_button = venster.maak_venster()

    # Koppel de knoppen aan de bijbehorende functies
    inlezen_A_button.config(command=inlezen_groep_A)

    # Start de tkinter mainloop om het venster weer te geven en op gebeurtenissen te reageren
    root.mainloop()

if __name__ == "__main__":
    main()
