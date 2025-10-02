import tkinter as tk
from tkinter import ttk

class Formulaire(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("800x500")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        content = tk.Frame(self)
        content.grid(row=0, column=0, sticky="nsew")

        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=10)
        content.rowconfigure(2, weight=1)
        content.columnconfigure(0, weight=1)

        header = tk.Frame(content)
        header.grid(row=0, column=0, sticky="nsew", padx=8, pady=2)
        header.rowconfigure(0, weight=1)
        header.columnconfigure(0, weight=1)
        header.columnconfigure(1, weight=2)
        header.columnconfigure(2, weight=3)

        main = tk.Frame(content)
        main.grid(row=1, column=0, sticky="nsew", padx=8, pady=2)
        main.columnconfigure(0, weight=2)
        main.columnconfigure(1, weight=4)
        main.columnconfigure(2, weight=2)
        main.columnconfigure(3, weight=1)
        main.columnconfigure(4, weight=3)
        main.rowconfigure(0, weight=1)
        main.rowconfigure(1, weight=10)

        footer = tk.Frame(content)
        footer.grid(row=2, column=0, sticky="nsew", padx=8, pady=2)
        footer.rowconfigure(0, weight=1)
        footer.columnconfigure(0, weight=1)
        footer.columnconfigure(1, weight=1)
        footer.columnconfigure(2, weight=1)
        footer.columnconfigure(3, weight=1)

        self.titre_nom = ttk.Label(header, text="Nom")
        self.titre_nom.grid(row=0, column=0, sticky="nsew")
        self.titre_email = ttk.Label(header, text="Email")
        self.titre_email.grid(row=0, column=1, sticky="nsew")
        self.titre_age = ttk.Label(header, text="Âge")
        self.titre_age.grid(row=0, column=2, sticky="nsew")


        self.nom_entry = ttk.Entry(main)
        self.nom_entry.grid(row=0, column=0, sticky="ew", padx=(0,2))
        self.email_entry = ttk.Entry(main)
        self.email_entry.grid(row=0, column=1, sticky="ew", padx=(2,2))
        self.age_entry = ttk.Entry(main)
        self.age_entry.grid(row=0, column=2, sticky="ew", padx=(2,8))
        self.ajouter_btn = ttk.Button(main, text="Ajouter")
        self.ajouter_btn.grid(row=0, column=3, padx=2, sticky="e")
        self.supprimer_selection_btn = ttk.Button(main, text="Supprimer la sélection")
        self.supprimer_selection_btn.grid(row=0, column=4, padx=(2,0) , sticky="e")

        self.tableau = ttk.Treeview(main, columns=("Nom", "Email", "Âge"), show="headings")
        self.tableau.heading("#1", text="Nom")
        self.tableau.heading("#2", text="Email")
        self.tableau.heading("#3", text="Âge")
        self.tableau.grid(columnspan=5, row=1, sticky="nsew")


        self.json_btn = ttk.Button(footer, text="Importer JSON")
        self.json_btn.grid(column=0, row=0, sticky="w")
        self.csv_btn = ttk.Button(footer, text="Importer CSV")
        self.csv_btn.grid(column=1, row=0, sticky="w")
        self.export_json_btn = ttk.Button(footer, text="Exporter JSON")
        self.export_json_btn.grid(column=2, row=0, sticky="e")
        self.export_csv_btn = ttk.Button(footer, text="Exporter CSV")
        self.export_csv_btn.grid(column=3, row=0, sticky="e")


if __name__ == "__main__":
    Formulaire().mainloop()