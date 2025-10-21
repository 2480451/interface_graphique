import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Produit:
    def __init__(self, nom , quantite, prix):
        self.nom = nom
        self.quantite = quantite
        self.prix = prix

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nom):
        if nom.strip() == "":
            raise ValueError("Le nom du produit ne peut pas être vide")
        self.__nom = nom

    @property
    def quantite(self):
        return self.__quantite

    @quantite.setter
    def quantite(self, quantite):
        if int(quantite) < 0:
            raise ValueError("La quantité doit être un entier positif")
        self.__quantite = quantite

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, prix):
        if float(prix) < 0:
            raise ValueError("La prix doit être un nombre réel positif")
        self.__prix = prix



class GestionnaireProduit(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des produits")
        self.geometry("800x540")
        self.rows = []
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.creer_widgets()

    def creer_widgets(self):
        self.frame = tk.Frame(self)
        self.frame.grid(row=0, column=0, sticky="ew")

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=2)

        # section ajouter un produit
        self.frm_ajout = ttk.LabelFrame(self.frame, text="Ajouter un produit")
        self.frm_ajout.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

        self.frm_ajout.columnconfigure(0, weight=1)
        self.frm_ajout.columnconfigure(1, weight=8)
        self.frm_ajout.columnconfigure(2, weight=1)
        self.frm_ajout.rowconfigure(0, weight=1)
        self.frm_ajout.rowconfigure(1, weight=1)
        self.frm_ajout.rowconfigure(2, weight=1)

        self.produit = ttk.Label(self.frm_ajout, text="Produit :")
        self.produit.grid(row=0, column=0, sticky="e", padx=5, pady=(10, 2))

        self.entry_produit = ttk.Entry(self.frm_ajout)
        self.entry_produit.grid(row=0, column=1, sticky="ew", padx=5, pady=(10, 2))

        self.quantite = ttk.Label(self.frm_ajout, text="Quantité :")
        self.quantite.grid(row=1, column=0, sticky="e", padx=5, pady=0)

        self.entry_quantite = ttk.Entry(self.frm_ajout)
        self.entry_quantite.grid(row=1, column=1, sticky="ew", padx=5, pady=0)

        self.prix = ttk.Label(self.frm_ajout, text="Prix :")
        self.prix.grid(row=2, column=0, sticky="e", padx=5, pady=(2, 10))

        self.entry_prix = ttk.Entry(self.frm_ajout)
        self.entry_prix.grid(row=2, column=1, sticky="ew", padx=5, pady=(2, 10))

        self.btn_ajouter = ttk.Button(self.frm_ajout, text="Ajouter Produit", command=self.ajouter_produit)
        self.btn_ajouter.grid(row=1, column=2, sticky="ew", padx=10, pady=5)



        # section gestion des produits
        self.frm_gestion = ttk.LabelFrame(self.frame, text="Gestion des produits")
        self.frm_gestion.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        self.frm_gestion.columnconfigure(0, weight=1)
        self.frm_gestion.columnconfigure(1, weight=1)
        self.frm_gestion.columnconfigure(2, weight=1)
        self.frm_gestion.columnconfigure(3, weight=1)
        self.frm_gestion.rowconfigure(0, weight=1)
        self.frm_gestion.rowconfigure(1, weight=1)

        self.supprimer = ttk.Button(self.frm_gestion, text="Supprimer Produit", command=self.supprimer)
        self.supprimer.grid(row=0, column=0, columnspan=2, sticky="ew", padx=100, pady=10)

        self.modifier = ttk.Button(self.frm_gestion, text="Modifier Produit", command=self.modifier)
        self.modifier.grid(row=0, column=2, columnspan=2, sticky="ew", padx=100, pady=10)

        self.sauvegarder_csv = ttk.Button(self.frm_gestion, text="Sauvegarder CSV")
        self.sauvegarder_csv.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        self.sauvegarder_json = ttk.Button(self.frm_gestion, text="Sauvegarder JSON")
        self.sauvegarder_json.grid(row=1, column=1, sticky="ew", padx=20, pady=10)

        self.importer_csv = ttk.Button(self.frm_gestion, text="Importer CSV")
        self.importer_csv.grid(row=1, column=2, sticky="ew", padx=20, pady=10)

        self.importer_json = ttk.Button(self.frm_gestion, text="Importer JSON")
        self.importer_json.grid(row=1, column=3, sticky="ew", padx=20, pady=10)


        #section du tableau des produits
        self.frm_tableau = tk.Frame(self.frame)
        self.frm_tableau.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
        self.frm_tableau.columnconfigure(0, weight=1)
        self.frm_tableau.rowconfigure(0, weight=1)

        self.tableau = ttk.Treeview(self.frm_tableau, columns=("Produit", "Quantité", "Prix"), show="headings", selectmode="extended")
        self.tableau.grid(row=0, column=0, sticky="ew", pady=10)

        self.tableau.heading("Produit", text="Produit")
        self.tableau.heading("Quantité", text="Quantité")
        self.tableau.heading("Prix", text="Prix")

        self.tableau.column("Produit")
        self.tableau.column("Quantité")
        self.tableau.column("Prix")

    def ajouter_produit(self):
        produit = self.entry_produit.get()
        quantite = self.entry_quantite.get()
        prix = self.entry_prix.get()
        if not produit:
            messagebox.showwarning("Validation", "Un nom de produit est requis.")
            return
        if not quantite:
            messagebox.showwarning("Validation", "Une quantité de produit est requise.")
            return
        if not prix:
            messagebox.showerror("Validation", "Un prix de produit est requis.")
            return

        self.tableau.insert("", "end", values=(produit, quantite, prix))

        self.rows.append({
            "Produit": produit,
            "Quantité": quantite,
            "Prix": prix
        })
        self.entry_produit.delete(0, "end")
        self.entry_quantite.delete(0, "end")
        self.entry_prix.delete(0, "end")

    def supprimer(self):
        selected_item = self.tableau.selection()
        if selected_item:
            for item in selected_item:
                self.tableau.delete(item)
        else:
            messagebox.showwarning("Avertissement", "Aucun élément sélectionné.")

    def modifier(self):
        selected_item = self.tableau.selection()
        if not selected_item:
            messagebox.showerror("Avertissement", "Aucun produit sélectionné!")
        item = selected_item[0]
        current_values = self.tableau.item(item, "values")
        produit, quantite, prix = current_values
        self.entry_produit.insert(0, produit)
        self.entry_quantite.insert(0, quantite)
        self.entry_prix.insert(0, prix)
        if selected_item:
            for item in selected_item:
                self.tableau.delete(item)


if __name__ == "__main__":
    app = GestionnaireProduit()
    app.mainloop()