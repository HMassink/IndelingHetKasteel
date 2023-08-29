from datetime import date
import tkinter as tk
from tkinter import ttk, messagebox
from py_vensters.knoppen import inlezen_spelers, uitlezen_spelers, toernooi_informatie, aanwezigheid_spelers, \
    indelen_ronde, verwijderen_ronde, uitslagen_ronde, ranglijst, opslaan, afsluiten
from py_database.db_connection import get_all_spelers, get_informatie, save_informatie


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

    def __init__(self, conn):

        self.conn = conn
        super().__init__()
        self.title("Indelen Het Kasteel")
        self.minsize(1920, 1080)
        self.uitgrijzen = False
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.tab_knoppen = ttk.Frame(self.notebook)
        self.tab_informatie = ttk.Frame(self.notebook)
        self.tab_aanwezige_spelers = ttk.Frame(self.notebook)
        self.tab_indeling = ttk.Frame(self.notebook)
        self.tab_stand_p1 = ttk.Frame(self.notebook)
        self.tab_stand_p2 = ttk.Frame(self.notebook)
        self.tab_stand_p3 = ttk.Frame(self.notebook)
        self.tab_jaarstand = ttk.Frame(self.notebook)
        self.tab_output = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_knoppen, text="Knoppen")
        self.notebook.add(self.tab_informatie, text="Informatie")
        self.notebook.add(self.tab_aanwezige_spelers, text="Aanwezige Spelers")
        self.notebook.add(self.tab_indeling, text="Indeling")
        self.notebook.add(self.tab_stand_p1, text="Stand P1")
        self.notebook.add(self.tab_stand_p2, text="Stand P2")
        self.notebook.add(self.tab_stand_p3, text="Stand P3")
        self.notebook.add(self.tab_jaarstand, text="Jaarstand")
        self.notebook.add(self.tab_output, text="Output")

        # Stel de breedte van de knoppen en de afstand tussen de knoppen in
        self.breedte_knop = 20
        self.afstand_knoppen = 5

        # Maak knoppen met de ingestelde breedte en afstand
        self.leegmaken_database_button = tk.Button(self.tab_knoppen, text="Leegmaken Database",
                                                command=lambda: inlezen_spelers(self, self.conn),
                                                width=self.breedte_knop)
        self.leegmaken_database_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.leegmaken_database_button_tooltip = ToolTip(self.leegmaken_database_button,
                                                      "Bestaande database leegmaken")

        self.maken_database_button = tk.Button(self.tab_knoppen, text="Maken Database",
                                                   command=lambda: inlezen_spelers(self, self.conn),
                                                   width=self.breedte_knop)
        self.maken_database_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.maken_database_button_tooltip = ToolTip(self.maken_database_button,
                                                         "Nieuwe Database maken")

        self.printen_database_button = tk.Button(self.tab_knoppen, text="Printen Database",
                                                   command=lambda: inlezen_spelers(self, self.conn),
                                                   width=self.breedte_knop)
        self.printen_database_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.printen_database_button_tooltip = ToolTip(self.printen_database_button,
                                                         "Bestaande database printen")
        self.backup_database_button = tk.Button(self.tab_knoppen, text="Backup Database",
                                                   command=lambda: inlezen_spelers(self, self.conn),
                                                   width=self.breedte_knop)
        self.backup_database_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.backup_database_button_tooltip = ToolTip(self.backup_database_button,
                                                         "Bestaande database backuppen")

        self.restore_database_button = tk.Button(self.tab_knoppen, text="Restore Database",
                                                   command=lambda: inlezen_spelers(self, self.conn),
                                                   width=self.breedte_knop)
        self.restore_database_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.restore_database_button_tooltip = ToolTip(self.restore_database_button,
                                                         "Bestaande database leegmaken")

        self.inlezen_spelers_button = tk.Button(self.tab_knoppen, text="Inlezen Spelers",
                                                command=lambda: inlezen_spelers(self, self.conn),
                                                width=self.breedte_knop)
        self.inlezen_spelers_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.inlezen_spelers_button_tooltip = ToolTip(self.inlezen_spelers_button,
                                                      "Tooltip tekst voor Inlezen Spelers knop")

        self.uitlezen_spelers_button = tk.Button(self.tab_knoppen, text="Uitlezen Spelers",
                                                 command=lambda: uitlezen_spelers(self), width=self.breedte_knop)
        self.uitlezen_spelers_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.uitlezen_spelers_button_tooltip = ToolTip(self.uitlezen_spelers_button,
                                                       "Tooltip tekst voor Uitlezen Spelers knop")

        self.toernooi_informatie_button = tk.Button(self.tab_knoppen, text="Toernooi Informatie",
                                                    command=lambda: toernooi_informatie(self), width=self.breedte_knop)
        self.toernooi_informatie_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.toernooi_informatie_button_tooltip = ToolTip(self.toernooi_informatie_button,
                                                          "Tooltip tekst voor Toernooi Informatie knop")

        self.aanwezigheid_spelers_button = tk.Button(self.tab_knoppen, text="Aanwezigheid Spelers",
                                                     command=lambda: aanwezigheid_spelers(self),
                                                     width=self.breedte_knop)
        self.aanwezigheid_spelers_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.aanwezigheid_spelers_button_tooltip = ToolTip(self.aanwezigheid_spelers_button,
                                                           "Tooltip tekst voor Aanwezigheid Spelers knop")

        self.indelen_ronde_button = tk.Button(self.tab_knoppen, text="Indelen Ronde",
                                              command=lambda: indelen_ronde(self), width=self.breedte_knop)
        self.indelen_ronde_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.indelen_ronde_button_tooltip = ToolTip(self.indelen_ronde_button, "Tooltip tekst voor Indelen Ronde knop")

        self.verwijderen_ronde_button = tk.Button(self.tab_knoppen, text="Verwijderen Ronde",
                                                  command=lambda: verwijderen_ronde(self), width=self.breedte_knop)
        self.verwijderen_ronde_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.verwijderen_ronde_button_tooltip = ToolTip(self.verwijderen_ronde_button,
                                                        "Tooltip tekst voor Verwijderen Ronde knop")

        self.uitslagen_ronde_button = tk.Button(self.tab_knoppen, text="Uitslagen Ronde",
                                                command=lambda: uitslagen_ronde(self), width=self.breedte_knop)
        self.uitslagen_ronde_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.uitslagen_ronde_button_tooltip = ToolTip(self.uitslagen_ronde_button,
                                                      "Tooltip tekst voor Uitslagen Ronde knop")

        self.ranglijst_button = tk.Button(self.tab_knoppen, text="Ranglijst", command=lambda: ranglijst(self),
                                          width=self.breedte_knop)
        self.ranglijst_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.ranglijst_button_tooltip = ToolTip(self.ranglijst_button, "Tooltip tekst voor Ranglijst knop")

        self.opslaan_button = tk.Button(self.tab_knoppen, text="Opslaan", command=lambda: opslaan(self),
                                        width=self.breedte_knop)
        self.opslaan_button.pack(anchor='w', pady=self.afstand_knoppen)
        self.opslaan_button_tooltip = ToolTip(self.opslaan_button, "Tooltip tekst voor Opslaan knop")

        self.afsluiten_button = tk.Button(self.tab_knoppen, text="Afsluiten", command=lambda: afsluiten(self),
                                          width=self.breedte_knop)
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

    def display_spelers_in_tab(self):
        """Display the players in the Aanwezige spelers tab."""
        for widget in self.tab_aanwezige_spelers.winfo_children():
            widget.destroy()  # Verwijder bestaande widgets om duplicatie te voorkomen

        # Haal de informatie uit de database
        info = get_informatie(self.conn)
        if info:
            seizoen, periode, ronde = info
        else:
            seizoen, periode, ronde = ("", "Leeg", "Leeg")

        # Datum label
        datum_label = ttk.Label(self.tab_aanwezige_spelers, text=f"{date.today().strftime('%d-%m-%Y')}")
        datum_label.grid(row=0, column=0, sticky='w', pady=(0, 10), padx=(0, 5))

        # Periode label
        periode_label = ttk.Label(self.tab_aanwezige_spelers, text="Periode")
        periode_label.grid(row=0, column=1, sticky='w', pady=(0, 10), padx=(5, 2.5))
        periode_value_label = ttk.Label(self.tab_aanwezige_spelers, text=f"{periode}")
        periode_value_label.grid(row=0, column=2, sticky='w', pady=(0, 10), padx=(2.5, 5))

        # Ronde label
        ronde_label = ttk.Label(self.tab_aanwezige_spelers, text="Ronde")
        ronde_label.grid(row=0, column=3, sticky='w', pady=(0, 10), padx=(5, 2.5))
        ronde_value_label = ttk.Label(self.tab_aanwezige_spelers, text=f"{ronde}")
        ronde_value_label.grid(row=0, column=4, sticky='w', pady=(0, 10), padx=(2.5, 5))

        spelers = get_all_spelers(self.conn)
        row_num = 1
        row_total = 1
        for speler in spelers:
            # Calculate the appropriate column based on the row number
            base_column = (row_total - 1) // 15 * 5

            # Nummer van de speler toevoegen
            speler_num_label = ttk.Label(self.tab_aanwezige_spelers, text=f"{speler[0]}")
            speler_num_label.grid(row=row_num, column=base_column, sticky='w', pady=2.5, padx=(0, 2.5))

            speler_label = ttk.Label(self.tab_aanwezige_spelers, text=f"{speler[2]} {speler[1]}")
            speler_label.grid(row=row_num, column=base_column + 1, sticky='w', pady=2.5, padx=(0, 2.5))

            groep_label = ttk.Label(self.tab_aanwezige_spelers, text=f"{speler[4]}")
            groep_label.grid(row=row_num, column=base_column + 2, sticky='w', pady=2.5, padx=(0, 2.5))

            # Bijgewerkte combobox keuzes
            speler_choice = ttk.Combobox(self.tab_aanwezige_spelers, values=["Aanwezig", "Afwezig", "Vrij", "Half punt"])
            speler_choice.grid(row=row_num, column=base_column + 3, sticky='w', pady=2.5, padx=(0, 2.5))
            speler_choice.set("Aanwezig")  # Stel 'Aanwezig' in als de standaard keuze

            # Groen label toevoegen
            green_label = ttk.Label(self.tab_aanwezige_spelers, background="green", width=2)
            green_label.grid(row=row_num, column=base_column + 4, sticky='w', pady=2.5, padx=(5, 15))

            # Tooltip toevoegen aan groen label
            ToolTip(green_label, "Rood : al vrij geweest")

            row_num = 1 if row_num == 15 else row_num + 1
            row_total += 1

        # "Verwerken" button
        verwerken_button = ttk.Button(self.tab_aanwezige_spelers, text="Verwerken")
        verwerken_button.grid(row=17, column=0, pady=10, columnspan=5, sticky="w")

        self.notebook.select(self.tab_aanwezige_spelers)  # Selecteer het tabblad 'Aanwezige Spelers' (tab_aanwezige_spelers)

    def clear_output(self):
        self.output_text.delete("1.0", tk.END)

    def setup_informatie_tab(self):
        """Set up the Informatie tab."""

        # Haal de toernooi-informatie op uit de database
        info = get_informatie(self.conn)

        # Pak de opgehaalde informatie uit
        seizoen, periode, ronde = info if info else ("", "Leeg", "Leeg")

        # Seizoen label en invoerveld
        seizoen_label = ttk.Label(self.tab_informatie, text="Seizoen")
        seizoen_label.grid(row=0, column=0, sticky='w', pady=(10, 5), padx=(10, 5))
        self.seizoen_entry = ttk.Entry(self.tab_informatie)
        self.seizoen_entry.insert(0, seizoen)  # Voeg de opgehaalde seizoen waarde in
        self.seizoen_entry.grid(row=0, column=1, sticky='w', pady=(10, 5), padx=(10, 5))

        # Periode label en invoerveld voor integer
        periode_label = ttk.Label(self.tab_informatie, text="Periode")
        periode_label.grid(row=1, column=0, sticky='w', pady=5, padx=(10, 5))
        self.periode_entry = ttk.Entry(self.tab_informatie)
        self.periode_entry.insert(0, periode)  # Voeg de opgehaalde periode waarde in
        self.periode_entry.grid(row=1, column=1, sticky='w', pady=5, padx=(10, 5))

        # Ronde label en invoerveld voor integer
        ronde_label = ttk.Label(self.tab_informatie, text="Ronde")
        ronde_label.grid(row=2, column=0, sticky='w', pady=5, padx=(10, 5))
        self.ronde_entry = ttk.Entry(self.tab_informatie)
        self.ronde_entry.insert(0, ronde)  # Voeg de opgehaalde ronde waarde in
        self.ronde_entry.grid(row=2, column=1, sticky='w', pady=5, padx=(10, 5))

        # Opslaan button
        opslaan_button = ttk.Button(self.tab_informatie, text="Opslaan", command=self.handle_opslaan_button_click)
        opslaan_button.grid(row=3, column=0, sticky='w', pady=(10, 5), padx=(10, 5))

        self.notebook.select(self.tab_informatie)


    def handle_opslaan_button_click(self):
        """Event handler for the 'Opslaan' button."""

        # Retrieve values from the fields
        seizoen = self.seizoen_entry.get()
        periode_value = self.periode_entry.get()
        ronde_value = self.ronde_entry.get()

        # Check if periode and ronde are integers
        try:
            periode = int(periode_value)
            ronde = int(ronde_value)
        except ValueError:
            messagebox.showerror("Fout", "Zorg ervoor dat zowel periode als ronde getallen zijn.")
            return

        # Save the information to the database
        save_informatie(self.conn, seizoen, periode, ronde)


if __name__ == "__main__":
    app = Hoofdvenster()
    app.mainloop()
