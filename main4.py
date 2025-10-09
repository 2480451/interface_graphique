
import tkinter as tk
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
        self.nom_entry = ttk.Entry(header_content)
        self.nom_entry.grid(row=1, column=0, sticky="ew", padx=(20, 5), pady=5)
        self.email_entry = ttk.Entry(header_content, width=30)
        self.email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
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
        nom = self.nom_entry.get()
        email = self.email_entry.get()
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
        self.nom_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
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
            return

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
        if not self.rows:
            messagebox.showinfo("Exporter CSV", "Rien à exporter")
            return

        path = filedialog.asksaveasfilename(title="Exporter CSV", defaultextension=".csv",
                                            filetypes=(("Csv", "*.csv"), ("All files", "*.*")))
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow(["nom", "email", "age"])
                for r in self.rows:
                    writer.writerow([r.nom, r.email, r.age])
            messagebox.showinfo("Exporter CSV", "Exportation CSV complétée.")

        except Exception as e:
            messagebox.showerror("Échec exportation CSV", str(e))

    def importer_csv(self):
        path = filedialog.askopenfilename(title="Importer CSV", filetypes=(("Csv", "*.csv"), ("All files", "*.*")))
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter=",")
                data = reader

            if not isinstance(data, list):
                raise ValueError("Le CSV doit contenir une liste d'objet.")
            self.rows = []
            for r in data:
                if isinstance(r, dict):
                    ligne = {}
                    for k in FIELDS:
                        ligne[k] = r.get(k, "")
                    self.rows.append(ligne)
            self.refresh()
            messagebox.showinfo("Importer CSV", "Importation CSV complétée.")
        except Exception as e:
            messagebox.showerror("Échec d'importation CSV", str(e))






if __name__ == "__main__":
    Formulaire().mainloop()