# exercice important
"""gestionnaire de stock
fiche article
statut combobox
isbn
auteur
**on peut changer le label ou le text d'un bouton selon L'option du combobox**
il faut acheter des produits avant de vendre des produits
si achat d'un meme article, lorsque saisi de l'isbn, complète les autres champs
mise à jour dans le treeview
"""

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# DB_PATH = "gestion_stock.db"

class Livre:
    def __init__(self, titre, auteur, isbn, statut):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
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
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        if value not in self.categorie_livre:
            raise ValueError("Le livre doit être classé dans une des catégorie reconnues :\n 'Roman', 'Essai', 'Science', 'Biographie', 'Technologie'.")
        self.__isbn = value

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
        self.title("Gestionnaire de Stock")
        self.create_widgets()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)

        self.ajout_possible = False
    #
    # def init_db(self):
    #     self.conn = sqlite3.connect(DB_PATH)
    #     cur = self.conn.cursor()
    #     cur.execute("""
    #     CREATE TABLE IF NOT EXISTS people(
    #     id integer PRIMARY KEY AUTOINCREMENT,
    #     isbn TEXT NOT NULL ,
    #     titre TEXT NOT NULL,
    #     auteur TEXT NOT NULL,
    #     quantite INTEGER NOT NULL
    #      )
    #     """)
    #     self.conn.commit()
    #
    # def _insert(self, isbn, titre, auteur, quantite):
    #     self.conn.execute(
    #         "INSERT INTO gestion_stock (isbn, titre, auteur, quantite) VALUES (?, ?, ?, ?)",
    #         (isbn, titre, auteur, quantite)
    #     )
    #     self.conn.commit()
    #
    # def _update(self, row_id, quantite):
    #     self.conn.execute(
    #         "UPDATE people SET quantite = ? WHERE id = ?",
    #         (quantite, row_id)
    #     )
    #     self.conn.commit()
    #
    # def _delete(self, row_id):
    #     self.conn.execute("DELETE FROM gestion_stock WHERE id = ?", (row_id,))
    #     self.conn.commit()
    #
    # def _fetch_all(self):
    #     cur = self.conn.cursor()
    #     cur.execute("SELECT id, isbn, titre, auteur, quantite FROM gestion_stock ORDER BY id DESC")
    #     return cur.fetchall()


    def create_widgets(self):
        # variable par défaut
        self.statut = tk.StringVar(value="Achat")

        # interface de fiche livre
        self.fiche_article = tk.LabelFrame(self, text="Fiche Article", relief="ridge", bd=3)
        self.fiche_article.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.fiche_article.columnconfigure(0, weight=1)
        self.fiche_article.columnconfigure(1, weight=2)
        self.fiche_article.rowconfigure(0, weight=1)
        self.fiche_article.rowconfigure(1, weight=1)
        self.fiche_article.rowconfigure(2, weight=1)
        self.fiche_article.rowconfigure(3, weight=1)
        self.fiche_article.rowconfigure(4, weight=2)
        self.fiche_article.rowconfigure(5, weight=1)



        self.label_isbn = ttk.Label(self.fiche_article, text="ISBN")
        self.label_isbn.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.entry_isbn = ttk.Entry(self.fiche_article)
        self.entry_isbn.grid(row=1, column=1, sticky="we", padx=10, pady=10)

        self.label_titre = ttk.Label(self.fiche_article, text="Titre")
        self.label_titre.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.entry_titre = ttk.Entry(self.fiche_article)
        self.entry_titre.grid(row=2, column=1, sticky="we", padx=10, pady=10)

        self.label_auteur = ttk.Label(self.fiche_article, text="Auteur")
        self.label_auteur.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.entry_auteur = ttk.Entry(self.fiche_article)
        self.entry_auteur.grid(row=3, column=1, sticky="we", padx=10, pady=10)

        self.label_quantité = tk.Label(self.fiche_article)
        self.label_quantité.grid(row=4, column=0, sticky="w", padx=10, pady=10)
        self.entry_quantité = ttk.Entry(self.fiche_article)
        self.entry_quantité.grid(row=4, column=1, sticky="we", padx=10, pady=10)

        self.label_statut = ttk.Label(self.fiche_article, text="Statut")
        self.label_statut.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.menu_statut = ttk.Combobox(self.fiche_article, textvariable=self.statut, values=["Vente", "Achat"])
        self.menu_statut.grid(row=0, column=1, sticky="we", padx=10, pady=10)
        self.menu_statut.bind("<<ComboboxSelected>>", self.update_label_button)


        #interface de outils de gestion inclus dans fiche livre
        self.outils_gestion = tk.LabelFrame(self.fiche_article, text="Outils de gestion")
        self.outils_gestion.grid(row=5, columnspan=2, padx=10, pady=10, sticky="ew")

        self.outils_gestion.columnconfigure(0, weight=1)
        self.outils_gestion.columnconfigure(1, weight=1)
        self.outils_gestion.rowconfigure(0, weight=1)
        self.outils_gestion.rowconfigure(1, weight=1)

        self.btn_ajouter = ttk.Button(self.outils_gestion, text="Ajouter", command=self.ajouter_livre)
        self.btn_ajouter.grid(row=0, column=0, padx=4, pady=4, sticky="ew")

        self.btn_modifier = ttk.Button(self.outils_gestion, text="Modifier", command=self.modifier_livre)
        self.btn_modifier.grid(row=0, column=1, padx=4, pady=4, sticky="ew")

        self.btn_supprimer = ttk.Button(self.outils_gestion, text="Supprimer", command=self.supprimer_livre)
        self.btn_supprimer.grid(row=1, column=0, padx=4, pady=4, sticky="ew")

        self.btn_quitter = ttk.Button(self.outils_gestion, text="Quitter", command=self.quitter_app)
        self.btn_quitter.grid(row=1, column=1, padx=4, pady=4, sticky="ew")


        # interface tableau des livres
        self.frm_tableau = tk.Frame(self, relief="ridge", bd=3)
        self.frm_tableau.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.frm_tableau.columnconfigure(0, weight=1)
        self.frm_tableau.rowconfigure(0, weight=1)

        self.columns = ("id", "isbn", "titre", "auteur", "quantite")
        self.tableau = ttk.Treeview(self.frm_tableau, columns=self.columns, show="headings")
        self.tableau.heading("id", text="ID")
        self.tableau.column("id", width=50)
        self.tableau.heading("isbn", text="ISBN")
        self.tableau.column("isbn", width=150)
        self.tableau.heading("titre", text="Titre")
        self.tableau.column("titre", width=200)
        self.tableau.heading("auteur", text="Auteur")
        self.tableau.column("auteur", width=200)
        self.tableau.heading("quantite", text="Quantité en stock")
        self.tableau.column("quantite", width=150)
        self.tableau.grid(row=0, column=0, sticky="nsew")
        self.update_label_button()

    def update_label_button(self, event=None):
        current_selection = self.statut.get()
        if current_selection == "Vente":
            self.label_quantité.config(text="Quantité vendue")
            self.btn_ajouter.config(text="Vendre")
        elif current_selection == "Achat":
            self.label_quantité.config(text="Quantité achetée")
            self.btn_ajouter.config(text="Acheter")

    def ajouter_livre(self):
        isbn = self.entry_isbn.get()
        titre = self.entry_titre.get()
        auteur = self.entry_auteur.get()
        quantite = self.entry_quantité
        pass

    def supprimer_livre(self):
        selected = self.tableau.selection()
        if not selected:
            messagebox.showwarning("Sélection requise", "Veuillez sélectionner un livre à supprimer.")
            return
        for item in selected:
            self.tableau.delete(item)

    def modifier_livre(self):
        pass


    def quitter_app(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()