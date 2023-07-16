
import os
import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk

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


def inlezen_spelers():
    # Implementeer de functie om de spelers in te lezen
    print("Inlezen Spelers knop is geklikt, implementeer de functie hier")


class Hoofdvenster(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Indelen Het Kasteel")

        # Stel de minimumgrootte van het hoofdvenster in
        self.minsize(1920, 1080)

        # Maak de tabbladen
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="nsew")

        # Configureer de grid-geometriemanager
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Voeg tabbladen toe
        self.tab_knoppen = ttk.Frame(self.notebook)
        self.tab_aanwezige_spelers = ttk.Frame(self.notebook)
        self.tab_indeling = ttk.Frame(self.notebook)
        self.tab_stand_p1 = ttk.Frame(self.notebook)
        self.tab_stand_p2 = ttk.Frame(self.notebook)
        self.tab_stand_p3 = ttk.Frame(self.notebook)
        self.tab_jaarstand = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_knoppen, text="Knoppen")
        self.notebook.add(self.tab_aanwezige_spelers, text="Aanwezige Spelers")
        self.notebook.add(self.tab_indeling, text="Indeling")
        self.notebook.add(self.tab_stand_p1, text="Stand P1")
        self.notebook.add(self.tab_stand_p2, text="Stand P2")
        self.notebook.add(self.tab_stand_p3, text="Stand P3")
        self.notebook.add(self.tab_jaarstand, text="Jaarstand")

        # Voeg de "Inlezen Spelers" knop toe aan het eerste tabblad (knoppen)
        self.inlezen_spelers_button = tk.Button(self.tab_knoppen, text="Inlezen Spelers", command=inlezen_spelers)
        self.inlezen_spelers_button.pack()


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
