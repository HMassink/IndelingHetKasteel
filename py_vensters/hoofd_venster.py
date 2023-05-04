import tkinter as tk
from tkinter import ttk
from py_vensters.knoppen import inlezen_spelers


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


if __name__ == "__main__":
    app = Hoofdvenster()
    app.mainloop()
