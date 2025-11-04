import tkinter as tk
from tkinter import ttk, messagebox, filedialog



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD Exemple")
        self.geometry("700x500")
        self.create_widgets()
        self.selected_id = None
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=10)


        self.ajout_possible = False


    def create_widgets(self):

        # interface de fiche
        self.fiche = ttk.LabelFrame(self, text="Fiche")
        self.fiche.grid(row=0, column=0, padx=10, pady=10, sticky="enw")

        self.fiche.columnconfigure(0, weight=1)
        self.fiche.columnconfigure(1, weight=4)
        self.fiche.columnconfigure(2, weight=1)
        self.fiche.columnconfigure(3, weight=4)
        self.fiche.columnconfigure(4, weight=1)
        self.fiche.columnconfigure(5, weight=1)

        self.fiche.rowconfigure(0, weight=1)
        self.fiche.rowconfigure(1, weight=1)


        self.label_nom = ttk.Label(self.fiche, text="Nom")
        self.label_nom.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nom = ttk.Entry(self.fiche)
        self.entry_nom.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.label_email = ttk.Label(self.fiche, text="Email")
        self.label_email.grid(row=0, column=2, padx=10, pady=10)
        self.entry_email = ttk.Entry(self.fiche)
        self.entry_email.grid(row=0, column=3, padx=10, pady=10, sticky="ew")
        self.label_age = ttk.Label(self.fiche, text="Âge")
        self.label_age.grid(row=0, column=4, padx=10, pady=10)
        self.entry_age = ttk.Entry(self.fiche)
        self.entry_age.grid(row=0, column=5, padx=10, pady=10, sticky="ew")

        self.frame_btn = ttk.Frame(self.fiche)
        self.frame_btn.grid(row=1, columnspan=6, sticky="nsew")
        self.frame_btn.columnconfigure(0, weight=1)
        self.frame_btn.columnconfigure(1, weight=1)
        self.frame_btn.columnconfigure(2, weight=1)
        self.frame_btn.columnconfigure(3, weight=1)

        self.btn_nouveau = ttk.Button(self.frame_btn, text="Nouveau")
        self.btn_nouveau.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.btn_ajouter = ttk.Button(self.frame_btn, text="Ajouter")
        self.btn_ajouter.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.btn_modifier = ttk.Button(self.frame_btn, text="Modifier")
        self.btn_modifier.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        self.btn_supprimer = ttk.Button(self.frame_btn, text="Supprimer")
        self.btn_supprimer.grid(row=1, column=3, padx=10, pady=10, sticky="ew")

        # interface tableau des livres
        self.frm_tableau = tk.Frame(self, bd=1)
        self.frm_tableau.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
        self.frm_tableau.columnconfigure(0, weight=1)
        self.frm_tableau.rowconfigure(0, weight=1)

        self.columns = ("id", "nom", "email", "age")
        self.tableau = ttk.Treeview(self.frm_tableau, columns=self.columns, show="headings")
        self.tableau.heading("id", text="ID")
        self.tableau.heading("nom", text="Nom")
        self.tableau.heading("email", text="Email")
        self.tableau.heading("age", text="Âge")
        self.tableau.grid(row=0, column=0, sticky="nsew")

    def init_db(self):
        pass

    def _insert(self, name, email, age):
        pass

    def _update(self, name, email, age):
        self.conn.execute("UPDATE people SET name = ? WHERE id = ?", (row_id, ))
        self.conn.commit()

    def _delete(self, row_id):
        pass

    def _fetch_all(self):
        pass

    def _validate(self):
        name = self.entry_nom.get()
        email = self.entry_email.get()
        age = self.entry_age.get()
        if not name or not email or not age:
            messagebox.showwarning("Erreur", "Tous les champs sont obligatoires")
            return
        if not age.isdigit():
            messagebox.showerror("Age invalide", "L'âge doit être un entier")
            return
        return name, email, int(age)

    def _clear_form(self):
        self.entry_nom.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_age.delete(0, "end")


    def _load_rows(self):
        for item in self.tableau.get_children():
            self.tableau.delete(item)

        for row in self._fetch_all():
            self._insert("", "", values=row)

    def _update_buttons(self):
        selection = self.selected_id


if __name__ == "__main__":
    app = App()
    app.mainloop()