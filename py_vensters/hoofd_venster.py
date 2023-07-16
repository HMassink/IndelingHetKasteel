import tkinter as tk
from tkinter import ttk
from py_vensters.knoppen import inlezen_spelers, uitlezen_spelers, toernooi_informatie, aanwezigheid_spelers, indelen_ronde, verwijderen_ronde, uitslagen_ronde, ranglijst, opslaan, afsluiten


class ToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.tooltipwindow = None

    def enter(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltipwindow = tk.Toplevel(self.widget)
        self.tooltipwindow.wm_overrideredirect(True)
        self.tooltipwindow.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tooltipwindow, text=self.text, background="#ffffe0", relief='solid', borderwidth=1)
        label.pack(ipadx=1)

    def leave(self, event=None):
        if self.tooltipwindow:
            self.tooltipwindow.destroy()
            self.tooltipwindow = None

class Hoofdvenster(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Indelen Het Kasteel")
        self.minsize(1920, 1080)
        self.uitgrijzen = False
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tab_knoppen = ttk.Frame(self.notebook)
        self.tab_aanwezige_spelers = ttk.Frame(self.notebook)
        self.tab_indeling = ttk.Frame(self.notebook)
        self.tab_stand_p1 = ttk.Frame(self.notebook)
        self.tab_stand_p2 = ttk.Frame(self.notebook)
        self.tab_stand_p3 = ttk.Frame(self.notebook)
        self.tab_jaarstand = ttk.Frame(self.notebook)
        self.tab_output = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_knoppen, text="Knoppen")
        self.notebook.add(self.tab_aanwezige_spelers, text="Aanwezige Spelers")
        self.notebook.add(self.tab_indeling, text="Indeling")
        self.notebook.add(self.tab_stand_p1, text="Stand P1")
        self.notebook.add(self.tab_stand_p2, text="Stand P2")
        self.notebook.add(self.tab_stand_p3, text="Stand P3")
        self.notebook.add(self.tab_jaarstand, text="Jaarstand")
        self.notebook.add(self.tab_output, text="Output")

        # Stel de breedte van de knoppen en de afstand tussen de knoppen in
        self.breedte_knop = 20
        self.afstand_knoppen = 10

        # Maak knoppen met de ingestelde breedte en afstand
        self.inlezen_spelers_button = tk.Button(self.tab_knoppen, text="Inlezen Spelers", command=lambda: inlezen_spelers(self), width=self.breedte_knop)
        self.inlezen_spelers_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.inlezen_spelers_button_tooltip = ToolTip(self.inlezen_spelers_button, "Tooltip tekst voor Inlezen Spelers knop")

        self.uitlezen_spelers_button = tk.Button(self.tab_knoppen, text="Uitlezen Spelers", command=lambda: uitlezen_spelers(self), width=self.breedte_knop)
        self.uitlezen_spelers_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.uitlezen_spelers_button_tooltip = ToolTip(self.uitlezen_spelers_button, "Tooltip tekst voor Uitlezen Spelers knop")

        self.toernooi_informatie_button = tk.Button(self.tab_knoppen, text="Toernooi Informatie", command=lambda: toernooi_informatie(self), width=self.breedte_knop)
        self.toernooi_informatie_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.toernooi_informatie_button_tooltip = ToolTip(self.toernooi_informatie_button, "Tooltip tekst voor Toernooi Informatie knop")

        self.aanwezigheid_spelers_button = tk.Button(self.tab_knoppen, text="Aanwezigheid Spelers", command=lambda: aanwezigheid_spelers(self), width=self.breedte_knop)
        self.aanwezigheid_spelers_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.aanwezigheid_spelers_button_tooltip = ToolTip(self.aanwezigheid_spelers_button, "Tooltip tekst voor Aanwezigheid Spelers knop")

        self.indelen_ronde_button = tk.Button(self.tab_knoppen, text="Indelen Ronde", command=lambda: indelen_ronde(self), width=self.breedte_knop)
        self.indelen_ronde_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.indelen_ronde_button_tooltip = ToolTip(self.indelen_ronde_button, "Tooltip tekst voor Indelen Ronde knop")

        self.verwijderen_ronde_button = tk.Button(self.tab_knoppen, text="Verwijderen Ronde", command=lambda: verwijderen_ronde(self), width=self.breedte_knop)
        self.verwijderen_ronde_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.verwijderen_ronde_button_tooltip = ToolTip(self.verwijderen_ronde_button, "Tooltip tekst voor Verwijderen Ronde knop")

        self.uitslagen_ronde_button = tk.Button(self.tab_knoppen, text="Uitslagen Ronde", command=lambda: uitslagen_ronde(self), width=self.breedte_knop)
        self.uitslagen_ronde_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.uitslagen_ronde_button_tooltip = ToolTip(self.uitslagen_ronde_button, "Tooltip tekst voor Uitslagen Ronde knop")

        self.ranglijst_button = tk.Button(self.tab_knoppen, text="Ranglijst", command=lambda: ranglijst(self), width=self.breedte_knop)
        self.ranglijst_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.ranglijst_button_tooltip = ToolTip(self.ranglijst_button, "Tooltip tekst voor Ranglijst knop")

        self.opslaan_button = tk.Button(self.tab_knoppen, text="Opslaan", command=lambda: opslaan(self), width=self.breedte_knop)
        self.opslaan_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.opslaan_button_tooltip = ToolTip(self.opslaan_button, "Tooltip tekst voor Opslaan knop")

        self.afsluiten_button = tk.Button(self.tab_knoppen, text="Afsluiten", command=lambda: afsluiten(self), width=self.breedte_knop)
        self.afsluiten_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.afsluiten_button_tooltip = ToolTip(self.afsluiten_button, "Tooltip tekst voor Opslaan knop")

        # Check de waarde van 'uitgrijzen' en update de knopstatus dienovereenkomstig
        if self.uitgrijzen:
            self.inlezen_spelers_button.config(state='disabled')
        else:
            self.inlezen_spelers_button.config(state='normal')

        # Voeg de 'Text' widget toe aan 'tab_output'
        self.output_text = tk.Text(self.tab_output)
        self.output_text.grid(sticky="nsew", row=0, column=0)

        # Voeg een 'Clear' knop toe aan 'tab_output'
        self.clear_button = tk.Button(self.tab_output, text="Clear", command=self.clear_output)
        self.clear_button.grid(row=1, column=0, sticky="se")

        # Configureer de rij en kolom van 'tab_output' om mee te groeien met het venster
        self.tab_output.grid_rowconfigure(0, weight=1)
        self.tab_output.grid_columnconfigure(0, weight=1)

    # Voeg een print-functie toe die tekst naar de 'Text' widget schrijft
    def print_to_output(self, text):
        self.output_text.insert(tk.END, text + "\n")

    # Voeg een clear-functie toe die de 'Text' widget leegmaakt
    def clear_output(self):
        self.output_text.delete("1.0", tk.END)

if __name__ == "__main__":
    app = Hoofdvenster()
    app.mainloop()
