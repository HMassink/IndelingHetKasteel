import tkinter as tk
from tkinter import ttk

def create_example_window():
    window = tk.Tk()
    window.title("Voorbeeld Venster")

    notebook = ttk.Notebook(window)
    tab1 = ttk.Frame(notebook)
    tab2 = ttk.Frame(notebook)
    notebook.add(tab1, text="Tab 1")
    notebook.add(tab2, text="Tab 2")
    notebook.pack(expand=True, fill="both")

    button1 = ttk.Button(tab1, text="Knop 1")
    button1.grid(row=0, column=0, padx=10, pady=10)

    button2 = ttk.Button(tab1, text="Knop 2")
    button2.grid(row=1, column=0, padx=10, pady=10)

    # Tabel in Tab 2
    columns = ("#1", "#2", "#3")
    tree = ttk.Treeview(tab2, columns=columns, show="headings")

    tree.heading("#1", text="Kolom 1")
    tree.heading("#2", text="Kolom 2")
    tree.heading("#3", text="Kolom 3")

    tree.column("#1", width=100, anchor=tk.CENTER)
    tree.column("#2", width=100, anchor=tk.CENTER)
    tree.column("#3", width=100, anchor=tk.CENTER)

    # Voorbeeld data
    data = [
        ("Rij 1 Kolom 1", "Rij 1 Kolom 2", "Rij 1 Kolom 3"),
        ("Rij 2 Kolom 1", "Rij 2 Kolom 2", "Rij 2 Kolom 3"),
        ("Rij 3 Kolom 1", "Rij 3 Kolom 2", "Rij 3 Kolom 3"),
    ]

    for item in data:
        tree.insert("", tk.END, values=item)

    tree.pack(padx=10, pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_example_window()
