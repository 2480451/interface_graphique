# Examen Intra
# Application Gestionnaire de Bibliothèque
# Édouard Desgagné | 2480451

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json


class Livre:
    def __init__(self, titre, auteur, categorie, statut):
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.statut = statut

    categorie_livre = ["Roman", "Essai", "Science", "Biographie", "Technologie"]
    statut_livre = ["Disponible", "Emprunté"]

    @property
    def titre(self):
        return self.__titre

    @titre.setter
    def titre(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le titre du produit doit être une chaîne de caractères non vide.")
        self.__titre = value

    @property
    def auteur(self):
        return self.__auteur

    @auteur.setter
    def auteur(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("L'auteur du produit doit être une chaîne de caractères non vide.")
        self.__auteur = value

    @property
    def categorie(self):
        return self.__categorie

    @categorie.setter
    def categorie(self, value):
        if value not in self.categorie_livre:
            raise ValueError("Le livre doit être classé dans une des catégorie reconnues :\n 'Roman', 'Essai', 'Science', 'Biographie', 'Technologie'.")
        self.__categorie = value

    @property
    def statut(self):
        return self.__statut

    @statut.setter
    def statut(self, value):
        if value not in self.statut_livre:
            raise ValueError("Le livre doit être assigné à un statut : 'Disponible' ou 'Emprunté'.")
        self.__statut = value


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de Bibliothèque")
        self.create_widgets()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)

        self.ajout_possible = False


    def create_widgets(self):
        # variable par défaut
        self.statut = tk.StringVar(value="Disponible")

        # interface de fiche livre
        self.fiche_livre = tk.LabelFrame(self, text="Fiche du livre", relief="ridge", bd=3)
        self.fiche_livre.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.fiche_livre.columnconfigure(0, weight=1)
        self.fiche_livre.columnconfigure(1, weight=2)
        self.fiche_livre.rowconfigure(0, weight=1)
        self.fiche_livre.rowconfigure(1, weight=1)
        self.fiche_livre.rowconfigure(2, weight=1)
        self.fiche_livre.rowconfigure(3, weight=1)
        self.fiche_livre.rowconfigure(4, weight=2)

        self.label_titre = ttk.Label(self.fiche_livre, text="Titre")
        self.label_titre.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.entry_titre = ttk.Entry(self.fiche_livre)
        self.entry_titre.grid(row=0, column=1, sticky="we", padx=10, pady=10)

        self.label_auteur = ttk.Label(self.fiche_livre, text="Auteur")
        self.label_auteur.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.entry_auteur = ttk.Entry(self.fiche_livre)
        self.entry_auteur.grid(row=1, column=1, sticky="we", padx=10, pady=10)

        self.label_categorie = ttk.Label(self.fiche_livre, text="Catégorie")
        self.label_categorie.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.menu_categorie = ttk.Combobox(self.fiche_livre, values=["Roman", "Essai", "Science", "Biographie", "Technologie"])
        self.menu_categorie.grid(row=2, column=1, sticky="we", padx=10, pady=10)

        self.label_statut = ttk.Label(self.fiche_livre, text="Statut")
        self.label_statut.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.menu_statut = ttk.Combobox(self.fiche_livre, textvariable=self.statut, values=["Disponible", "Emprunté"])
        self.menu_statut.grid(row=3, column=1, sticky="we", padx=10, pady=10)

        #interface de outils de gestion inclus dans fiche livre
        self.outils_gestion = tk.LabelFrame(self.fiche_livre, text="Outils de gestion")
        self.outils_gestion.grid(row=4, columnspan=2, padx=10, pady=10, sticky="ew")

        self.outils_gestion.columnconfigure(0, weight=1)
        self.outils_gestion.columnconfigure(1, weight=1)
        self.outils_gestion.columnconfigure(2, weight=1)
        self.outils_gestion.rowconfigure(0, weight=1)
        self.outils_gestion.rowconfigure(1, weight=1)

        self.btn_nouveau = ttk.Button(self.outils_gestion, text="Nouveau", command=self.nouveau_livre)
        self.btn_nouveau.grid(row=0, column=0, padx=4, pady=4, sticky="ew")

        self.btn_ajouter = ttk.Button(self.outils_gestion, text="Ajouter", command=self.ajouter_livre)
        self.btn_ajouter.grid(row=0, column=1, padx=4, pady=4, sticky="ew")

        self.btn_supprimer = ttk.Button(self.outils_gestion, text="Supprimer", command=self.supprimer_livre)
        self.btn_supprimer.grid(row=0, column=2, padx=4, pady=4, sticky="ew")

        self.btn_importer_json = ttk.Button(self.outils_gestion, text="Importer JSON", command=self.importer_json)
        self.btn_importer_json.grid(row=1, column=0, padx=4, pady=4, sticky="ew")

        self.btn_exporter_json = ttk.Button(self.outils_gestion, text="Exporter JSON", command=self.exporter_json)
        self.btn_exporter_json.grid(row=1, column=1, padx=4, pady=4, sticky="ew")

        self.btn_quitter = ttk.Button(self.outils_gestion, text="Quitter", command=self.quitter_app)
        self.btn_quitter.grid(row=1, column=2, padx=4, pady=4, sticky="ew")


        # interface tableau des livres
        self.frm_tableau = tk.Frame(self, relief="ridge", bd=3)
        self.frm_tableau.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.frm_tableau.columnconfigure(0, weight=1)
        self.frm_tableau.rowconfigure(0, weight=1)

        self.columns = ("titre", "auteur", "categorie", "disponibilite")
        self.tableau = ttk.Treeview(self.frm_tableau, columns=self.columns, show="headings")
        self.tableau.heading("titre", text="Titre")
        self.tableau.heading("auteur", text="Auteur")
        self.tableau.heading("categorie", text="Catégorie")
        self.tableau.heading("disponibilite", text="Disponibilité")
        self.tableau.grid(row=0, column=0, sticky="nsew")

    def ajouter_livre(self):
        titre = self.entry_titre.get()
        auteur = self.entry_auteur.get()
        categorie = self.menu_categorie.get()
        statut = self.menu_statut.get()

        contenu = self.tableau.get_children()

        if (contenu and self.ajout_possible) or (not contenu):
            try:
                livre = Livre(titre, auteur, categorie, statut)
                self.tableau.insert("", "end", values=(livre.titre, livre.auteur, livre.categorie, livre.statut))
                self.entry_titre.delete(0, "end")
                self.entry_auteur.delete(0, "end")
                self.menu_categorie.delete(0, "end")
                self.menu_statut.delete(0, "end")
                self.ajout_possible = False

            except ValueError as e:
                messagebox.showerror("Erreur de saisie", str(e))

        elif contenu and not self.ajout_possible:
            messagebox.showwarning("Action requise", "Le tableau contient déjà des livres.\n"
                                                     "Cliquez sur 'Nouveau' avant d'ajouter un autre.")

    def supprimer_livre(self):
        selected = self.tableau.selection()
        if not selected:
            messagebox.showwarning("Sélection requise", "Veuillez sélectionner un livre à supprimer.")
            return
        for item in selected:
            self.tableau.delete(item)

    def nouveau_livre(self):
        self.entry_titre.delete(0, "end")
        self.entry_auteur.delete(0, "end")
        self.menu_categorie.delete(0, "end")
        self.menu_statut.delete(0, "end")
        self.ajout_possible = True
        messagebox.showinfo("Mode nouveau", "Vous pouvez maintenant ajouter un nouveau livre.")

    def exporter_json(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if not filepath:
            return
        data = []
        for row in self.tableau.get_children():
            data.append(dict(zip(self.columns, self.tableau.item(row)["values"])))
        with open(filepath, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        messagebox.showinfo("Succès", "Livres sauvegardés en JSON.")

    def importer_json(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if not filepath:
            return

        with open(filepath, mode='r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            messagebox.showerror("Erreur JSON", "Le fichier JSON doit contenir une liste d'objets.")
            return

        for item in data:
            livre = Livre(item["titre"], item["auteur"], item["categorie"], item["disponibilite"])
            self.tableau.insert("", "end", values=(livre.titre, livre.auteur, livre.categorie, livre.statut))

        messagebox.showinfo("Succès", "Importation JSON terminée")


    def quitter_app(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
