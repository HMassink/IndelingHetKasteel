import tkinter as tk

def maak_venster():
    # Maak het hoofdvenster
    root = tk.Tk()

    # Stel de grootte van het venster in op 1600 * 1200 pixels
    root.geometry("1600x1200")

    # Voeg de tekst "Indelingsprogramma Het Kasteel" toe bovenaan, in het midden van het venster met grotere letters
    tk.Label(root, text="Indelingsprogramma Het Kasteel", font=("Helvetica", 24)).pack(side="top", pady=20)

    # Maak een frame om de knoppen in te plaatsen
    knoppen_frame = tk.Frame(root)
    knoppen_frame.pack(side="left", padx=20, pady=20)

    # Maak een knop om de spelers in te lezen
    inlezen_spelers_button = tk.Button(knoppen_frame, text="Inlezen spelers")
    inlezen_spelers_button.pack(side="top", pady=10)

    # Plaats de frame aan de linkerkant, bovenin het venster
    knoppen_frame.place(x=10, y=50)

    return root, inlezen_spelers_button  # Geef het vensterobject en de knop terug aan het hoofdscript


def toon_spelers(spelers):
    # Maak een nieuw venster
    spelers_venster = tk.Toplevel()

    # Geef het venster een titel
    spelers_venster.title("Spelers Groep A")

    # Maak een canvas en een scrollbar
    canvas = tk.Canvas(spelers_venster, height=500)
    scrollbar = tk.Scrollbar(spelers_venster, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Plaats de canvas en scrollbar in het venster
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Maak een frame om alle spelerframes in te plaatsen
    container_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=container_frame, anchor="nw")

    # Maak een lijst met de mogelijke opties voor elke speler
    opties = ["aanwezig", "afwezig", "vrij", "1 punt", "0 punt", "0,5 punt"]

    # Bepaal een minimale breedte voor de kolom met de spelerlabels
    min_breedte = 200

    selected_options = []  # Voeg deze regel toe om de lijst van StringVar objecten bij te houden

    # Loop door de spelersA lijst en voeg de nummers, namen en keuzelijsten toe aan het venster
    for speler in spelers:
        nummer, naam, voornaam, elo = speler  # Voeg 'nummer' toe aan de unpacking

        # Maak een frame voor het nummer, de naam en de keuzelijst
        speler_frame = tk.Frame(container_frame)
        speler_frame.pack(anchor="w", padx=5, pady=5)

        # Maak een label met het nummer, de naam en de voornaam van de speler en voeg deze toe aan het frame
        speler_label = tk.Label(speler_frame, text=f"{nummer}. {naam} {voornaam}")  # Voeg het nummer toe aan de tekst
        speler_label.grid(row=0, column=0, sticky="w")

        # Stel de minimale breedte in voor de kolom met de spelerlabels
        speler_frame.grid_columnconfigure(0, minsize=min_breedte)

        # Maak een StringVar om de geselecteerde optie voor de speler op te slaan
        selected_option = tk.StringVar()
        selected_option.set(opties[0])  # Stel de standaardoptie in op 'aanwezig'

        # Maak een keuzelijst met de opties en voeg deze toe aan het frame
        option_menu = tk.OptionMenu(speler_frame, selected_option, *opties)
        option_menu.grid(row=0, column=1, sticky="e")

        # Voeg het StringVar object toe aan de lijst
        selected_options.append(selected_option)

    # Werk de scrollregion bij wanneer de canvas verandert
    container_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    def verwerk_aanwezigheid():
        gekozen_opties = []
        for speler, selected_option in zip(spelers, selected_options):
            nummer, naam, voornaam, elo = speler
            gekozen_optie = (nummer, naam, voornaam, selected_option.get())
            gekozen_opties.append(gekozen_optie)

        print("De volgende opties zijn gekozen:")
        print(gekozen_opties)  # Verwijder deze regel of vervang deze door een gewenste actie met de lijst 'gekozen_opties'
        schrijf_gekozen_opties(gekozen_opties)

    def schrijf_gekozen_opties(gekozen_opties):
        with open("gekozen_opties.txt", "w") as file:
            for optie in gekozen_opties:
                nummer, naam, voornaam, gekozen_optie = optie
                formatted_line = "{:<6}\t{:<20}\t{:<20}\t{:<10}\n".format(
                    nummer, naam, voornaam, gekozen_optie
                )
                file.write(formatted_line)

    def lees_gekozen_opties():
        gekozen_opties = []

        with open("gekozen_opties.txt", "r") as file:
            for line in file:
                # Verwijder witruimte en splits de regel op tabs
                nummer, naam, voornaam, gekozen_optie = line.strip().split('\t')

                # Verwijder alle spaties na de tekst in elke kolom
                nummer = nummer.rstrip()
                naam = naam.rstrip()
                voornaam = voornaam.rstrip()
                gekozen_optie = gekozen_optie.rstrip()

                # Converteer het nummer naar een integer
                nummer = int(nummer)

                # Voeg het nummer, naam, voornaam en gekozen_optie toe aan de gekozen_opties lijst
                gekozen_opties.append((nummer, naam, voornaam, gekozen_optie))

        print("De volgende opties zijn ingelezen:")
        print(gekozen_opties)  # Verwijder deze regel of vervang deze door een gewenste actie met de lijst 'gekozen_opties'

        return gekozen_opties

    # Maak een knop om de gekozen opties in te lezen en voeg deze toe aan het venster
    inlezen_opties_button = tk.Button(spelers_venster, text="Inlezen gekozen opties", command=lees_gekozen_opties)
    inlezen_opties_button.pack(side="bottom", anchor="w", pady=10)

    # Maak een knop om de aanwezigheid van spelers te verwerken en voeg deze toe aan het venster
    verwerk_button = tk.Button(spelers_venster, text="Verwerk aanwezigheid", command=verwerk_aanwezigheid)
    verwerk_button.pack(side="bottom", anchor="w", pady=10)

    # Toon het venster
    spelers_venster.mainloop()
