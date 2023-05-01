import tkinter as tk
from tkinter import ttk

def print_value(value):
    print(f"Ingegeven waarde: {value}")

def update_progressbar(progressbar):
    progressbar["value"] += 10
    if progressbar["value"] > 100:
        progressbar["value"] = 0
    progressbar.update_idletasks()

def maak_voorbeeld_venster():
    venster = tk.Tk()
    venster.title("Voorbeeldvenster")

    # Button
    knop = tk.Button(venster, text="Druk op mij", command=lambda: print_value("Button"))
    knop.grid(row=0, column=0, sticky="w")

    # Checkbutton
    check_var = tk.IntVar()
    checkbutton = tk.Checkbutton(venster, text="Vink mij aan", variable=check_var, command=lambda: print_value(f"Checkbutton: {check_var.get()}"))
    checkbutton.grid(row=1, column=0, sticky="w")

    # Radiobutton
    radio_var = tk.IntVar()
    radio1 = tk.Radiobutton(venster, text="Optie 1", variable=radio_var, value=1, command=lambda: print_value(f"Radiobutton: {radio_var.get()}"))
    radio1.grid(row=2, column=0, sticky="w")

    radio2 = tk.Radiobutton(venster, text="Optie 2", variable=radio_var, value=2, command=lambda: print_value(f"Radiobutton: {radio_var.get()}"))
    radio2.grid(row=3, column=0, sticky="w")

    # Entry
    entry = tk.Entry(venster)
    entry.grid(row=4, column=0, sticky="w")

    entry_button = tk.Button(venster, text="Submit Entry", command=lambda: print_value(f"Entry: {entry.get()}"))
    entry_button.grid(row=5, column=0, sticky="w")

    # Scale
    scale = tk.Scale(venster, from_=0, to=100, orient=tk.HORIZONTAL)
    scale.grid(row=6, column=0, sticky="w")

    scale_button = tk.Button(venster, text="Submit Scale", command=lambda: print_value(f"Scale: {scale.get()}"))
    scale_button.grid(row=7, column=0, sticky="w")

    # Dropdown (ComboBox)
    dropdown = ttk.Combobox(venster, values=["Optie 1", "Optie 2", "Optie 3"])
    dropdown.grid(row=8, column=0, sticky="w", pady=(0, 10))

    dropdown_button = tk.Button(venster, text="Submit Dropdown", command=lambda: print_value(f"Dropdown: {dropdown.get()}"))
    dropdown_button.grid(row=9, column=0, sticky="w", pady=(0, 10))

    # Spinbox
    spinbox = tk.Spinbox(venster, from_=0, to=100)
    spinbox.grid(row=10, column=0, sticky="w", pady=(0, 10))

    spinbox_button = tk.Button(venster, text="Submit Spinbox", command=lambda: print_value(f"Spinbox: {spinbox.get()}"))
    spinbox_button.grid(row=11, column=0, sticky="w", pady=(0, 10))

    # Progressbar
    progressbar = ttk.Progressbar(venster, orient="horizontal", length=200, mode="determinate")
    progressbar.grid(row=12, column=0, sticky="w", pady=(0, 10))

    progressbar_button = tk.Button(venster, text="Update Progressbar", command=lambda: update_progressbar(progressbar))
    progressbar_button.grid(row=13, column=0, sticky="w", pady=(0, 10))

    venster.mainloop()

