# import tkinter as tk
# from tkinter import ttk
#
# class Formulaire(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Formulaire")
#         self.geometry("800x500")
#
#         self.columnconfigure(0, weight=1)
#         self.rowconfigure(0, weight=1)
#
#         content = tk.Frame(self)
#         content.grid(row=0, column=0, sticky="nsew")
#
#         content.rowconfigure(0, weight=1)
#         content.rowconfigure(1, weight=10)
#         content.rowconfigure(2, weight=1)
#         content.columnconfigure(0, weight=1)
#
#         header = tk.Frame(content)
#         header.grid(row=0, column=0, sticky="nsew", padx=8, pady=2)
#         header.rowconfigure(0, weight=1)
#         header.columnconfigure(0, weight=1)
#         header.columnconfigure(1, weight=2)
#         header.columnconfigure(2, weight=3)
#
#         main = tk.Frame(content)
#         main.grid(row=1, column=0, sticky="nsew", padx=8, pady=2)
#         main.columnconfigure(0, weight=2)
#         main.columnconfigure(1, weight=4)
#         main.columnconfigure(2, weight=2)
#         main.columnconfigure(3, weight=1)
#         main.columnconfigure(4, weight=3)
#         main.rowconfigure(0, weight=1)
#         main.rowconfigure(1, weight=10)
#
#         footer = tk.Frame(content)
#         footer.grid(row=2, column=0, sticky="nsew", padx=8, pady=2)
#         footer.rowconfigure(0, weight=1)
#         footer.columnconfigure(0, weight=1)
#         footer.columnconfigure(1, weight=1)
#         footer.columnconfigure(2, weight=1)
#         footer.columnconfigure(3, weight=1)
#
#         self.titre_nom = ttk.Label(header, text="Nom")
#         self.titre_nom.grid(row=0, column=0, sticky="nsew")
#         self.titre_email = ttk.Label(header, text="Email")
#         self.titre_email.grid(row=0, column=1, sticky="nsew")
#         self.titre_age = ttk.Label(header, text="Âge")
#         self.titre_age.grid(row=0, column=2, sticky="nsew")
#
#
#         self.nom_entry = ttk.Entry(main)
#         self.nom_entry.grid(row=0, column=0, sticky="ew", padx=(0,2))
#         self.email_entry = ttk.Entry(main)
#         self.email_entry.grid(row=0, column=1, sticky="ew", padx=(2,2))
#         self.age_entry = ttk.Entry(main)
#         self.age_entry.grid(row=0, column=2, sticky="ew", padx=(2,8))
#         self.ajouter_btn = ttk.Button(main, text="Ajouter")
#         self.ajouter_btn.grid(row=0, column=3, padx=2, sticky="e")
#         self.supprimer_selection_btn = ttk.Button(main, text="Supprimer la sélection")
#         self.supprimer_selection_btn.grid(row=0, column=4, padx=(2,0) , sticky="e")
#
#         self.tableau = ttk.Treeview(main, columns=("Nom", "Email", "Âge"), show="headings")
#         self.tableau.heading("#1", text="Nom")
#         self.tableau.heading("#2", text="Email")
#         self.tableau.heading("#3", text="Âge")
#         self.tableau.grid(columnspan=5, row=1, sticky="nsew")
#
#
#         self.json_btn = ttk.Button(footer, text="Importer JSON")
#         self.json_btn.grid(column=0, row=0, sticky="w")
#         self.csv_btn = ttk.Button(footer, text="Importer CSV")
#         self.csv_btn.grid(column=1, row=0, sticky="w")
#         self.export_json_btn = ttk.Button(footer, text="Exporter JSON")
#         self.export_json_btn.grid(column=2, row=0, sticky="e")
#         self.export_csv_btn = ttk.Button(footer, text="Exporter CSV")
#         self.export_csv_btn.grid(column=3, row=0, sticky="e")
#

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk, filedialog
import json, csv
import re

FIELDS = ("nom", "email", "age")


class Formulaire(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("700x450")
        self.init_widgets()
        self.rows = []

    def init_widgets(self):

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        header_content = ttk.Frame(self)
        header_content.grid(row=0, column=0, sticky="ew")
        header_content.columnconfigure(0, weight=1)
        header_content.columnconfigure(1, weight=1)
        header_content.columnconfigure(2, weight=1)

        # labels
        self.Nom = ttk.Label(header_content, text="Nom")
        self.Nom.grid(row=0, column=0, sticky="w", padx=20, pady=5)
        self.Email = ttk.Label(header_content, text="Email")
        self.Email.grid(row=0, column=1, sticky="w", padx=20, pady=5)
        self.Age = ttk.Label(header_content, text="Âge")
        self.Age.grid(row=0, column=2, sticky="w", padx=20, pady=5)

        # inputs
        self.Nom_Entry = ttk.Entry(header_content)
        self.Nom_Entry.grid(row=1, column=0, sticky="ew", padx=(20, 5), pady=5)
        self.Email_Entry = ttk.Entry(header_content, width=30)
        self.Email_Entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        self.Age_Entry = ttk.Entry(header_content)
        self.Age_Entry.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

        # buttons
        self.Btn_Ajouter = ttk.Button(header_content, text="Ajouter", command=self.ajouter)
        self.Btn_Ajouter.grid(row=1, column=3, sticky="e", padx=5, pady=5)
        self.Btn_Supprimer = ttk.Button(header_content, text="Supprimer sélection", command=self.supprimer)
        self.Btn_Supprimer.grid(row=1, column=4, sticky="e", padx=(5, 20), pady=5)

        main_content = ttk.Frame(self)
        main_content.grid(row=1, column=0, sticky="snew")
        # Configurer les poids de la grille pour que le Treeview s'Ã©tire bien
        main_content.columnconfigure(0, weight=1)
        main_content.rowconfigure(0, weight=1)

        self.tree = ttk.Treeview(main_content, columns=("nom", "email", "age"), show="headings",
                                 selectmode="extended", )
        self.tree.heading("nom", text="Nom")
        self.tree.heading("email", text="Email")
        self.tree.heading("age", text="Âge")

        self.tree.column("nom", width=200)
        self.tree.column("email", width=380)
        self.tree.column("age", width=80)

        self.tree.grid(row=0, column=0, padx=20, pady=20, sticky="snew")

        footer_content = ttk.Frame(self)
        footer_content.grid(row=2, column=0, sticky="snew")
        footer_content.columnconfigure(1, weight=1)
        footer_content.columnconfigure(2, weight=1)
        self.Btn_Importer_Json = ttk.Button(footer_content, command=self.importer_json, text="Importer JSON")
        self.Btn_Importer_Json.grid(row=0, column=0, sticky="w", padx=(20, 5), pady=5)
        self.Btn_Importer_CSV = ttk.Button(footer_content, command=self.importer_csv, text="Importer CSV")
        self.Btn_Importer_CSV.grid(row=0, column=1, sticky="w", padx=5, pady=5)

        self.Btn_Exporter_Json = ttk.Button(footer_content, text="Exporter JSON", command=self.exporter_json)
        self.Btn_Exporter_Json.grid(row=0, column=3, sticky="e", padx=5, pady=5)
        self.Btn_Exporter_CSV = ttk.Button(footer_content, text="Exporter CSV", command=self.exporter_csv)
        self.Btn_Exporter_CSV.grid(row=0, column=4, sticky="e", padx=(5, 20), pady=5)

    def ajouter(self):
        nom = self.Nom_Entry.get()
        email = self.Email_Entry.get()
        age = self.Age_Entry.get()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not nom:
            messagebox.showwarning("Validation", "Le nom est requis.")
            return
        if not re.match(pattern, email):
            messagebox.showwarning("Validation", "Vérifier votre email.")
            return
        if age and not age.isdigit():
            messagebox.showerror("Validation", "Âge doit être un entier.")
            return

        self.tree.insert("", "end", values=(nom, email, age))
        self.rows.append({
            "nom": nom,
            "email": email,
            "age": age
        })
        self.Nom_Entry.delete(0, "end")
        self.Email_Entry.delete(0, "end")
        self.Age_Entry.delete(0, "end")

    def supprimer(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                self.tree.delete(item)
        else:
            messagebox.showwarning("Avertissement", "Aucun élément sélectionné.")


    def exporter_json(self):
        if not self.rows:
            messagebox.showinfo("Exporter JSON", "Rien à exporter")

        path = filedialog.asksaveasfilename(title="Exporter JSON", defaultextension=".json", filetypes=(("Json", "*.json"), ("All files", "*.*")))
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.rows, f, indent=4)
            messagebox.showinfo("Exporter JSON", "Exportation JSON complétée.")

        except Exception as e:
            messagebox.showerror("Échec exportation JSON", str(e))


    def importer_json(self):
        path = filedialog.askopenfilename(title="Importer JSON", filetypes=(("Json", "*.json"), ("All files", "*.*")))
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Le JSON doit contenir une liste d'objet.")
            self.rows = []
            for r in data:
                if isinstance(r, dict):
                    ligne = {}
                    for k in FIELDS:
                        ligne[k] = r.get(k, "")
                    self.rows.append(ligne)
            self.refresh()
            messagebox.showinfo("Importer JSON", "Importation JSON complétée.")
        except Exception as e:
            messagebox.showerror("Échec d'importation JSON", str(e))

    def refresh(self):
        enfants = self.tree.get_children()
        for enfant in enfants:
            self.tree.delete(enfant)

        for r in self.rows:
            nom = r.get("nom", "")
            email = r.get("email", "")
            age = r.get("age", "")

            self.tree.insert("", "end", values=(nom, email, age))




    def exporter_csv(self):
        pass

    def importer_csv(self):
        pass
if __name__ == "__main__":
    Formulaire().mainloop()