import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

DB_PATH = "member.db"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("360x180")
        self._init_db()
        self._build_ui()

    def _init_db(self):
        self.conn = sqlite3.connect(DB_PATH)
        cur = self.conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS member
                    (
                        id
                        INTEGER
                        PRIMARY
                        KEY
                        AUTOINCREMENT,
                        first_name
                        TEXT
                        NOT
                        NULL,
                        last_name
                        TEXT
                        NOT
                        NULL,
                        email
                        TEXT
                        NOT
                        NULL
                        UNIQUE,
                        password
                        TEXT
                        NOT
                        NULL
                    )
                    """)
        self.conn.commit()

    def _insert(self, nom, prenom, email, mdp):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO member(first_name, last_name, email, password) VALUES (?, ?, ?, ?)", (nom, prenom, email, mdp))
        self.conn.commit()


    def _fetch_one(self, email):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM member WHERE email = ?", (email,))
        return cursor.fetchone()


    def _build_ui(self):
        # La fenêtre principale s'étire
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Instancier le formulaire (LabelFrame)
        form = ttk.LabelFrame(self, text="Formulaire")
        form.grid(row=0, column=0, padx=12, pady=12, sticky="nsew")

        form.columnconfigure(1, weight=1)
        form.rowconfigure(0, weight=1)

        ttk.Label(form, text="Email :").grid(row=0, column=0, padx=(6, 8), pady=6, sticky="e")
        self.login_email = ttk.Entry(form)
        self.login_email.grid(row=0, column=1, padx=0, pady=6, sticky="ew")

        ttk.Label(form, text="Mot de passe :").grid(row=1, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_pass = ttk.Entry(form, show="*")
        self.ent_pass.grid(row=1, column=1, padx=0, pady=6, sticky="ew")

        self.btn_login = ttk.Button(form, text="Se connecter", command=self.ouvrir_espace_travail)
        self.btn_signin = ttk.Button(form, text="S'inscrire", command=self.ouvrir_espace_inscription)
        # rowspan=2 pour centrer verticalement entre Nom/Email
        self.btn_login.grid(row=2, column=0, columnspan=2, padx=(80, 0), pady=6, sticky="w")
        self.btn_signin.grid(row=2, column=1, columnspan=2, padx=(0, 80), pady=6, sticky="e")

    def ouvrir_espace_travail(self):
        email = self.login_email.get().strip()
        mdp_ent = self.ent_pass.get().strip()

        if not email or not mdp_ent:
            messagebox.showwarning("Champ requis", "Veuillez saisir l'email et le mot de passe.")
            return
        try:
            self._fetch_one(email)

        except sqlite3.OperationalError:
            messagebox.showerror("Connexion", "Email introuvable.")
            return
        mdp_db = self._fetch_one(email)
        if mdp_ent != mdp_db:
            messagebox.showerror("Connexion", "Mot de passe incorrect")

        else:
            self.withdraw()
            win_travail = tk.Toplevel(self)
            win_travail.title("Espace de travail")
            win_travail.geometry("520x420")
            win_travail.columnconfigure(0, weight=1)
            label = ttk.Label(win_travail, text="Bienvenue dans votre espace de travail !")
            label.grid(column=0, sticky="sn")


        """
        TODO: vérifier les identifiants saisis et afficher la bonne info.
        Étapes attendues:
        1) Récupérer email + mot de passe depuis les champs
           - si l’un est vide: messagebox.showwarning("Champs requis", "Veuillez saisir l'email et le mot de passe.")
        2) Vérifier l'émail et le mot de passe saisi depuis les champs avec celle qui existe dans la base de données
           - si l'émail n'existe pas dans la table member afficher: messagebox.showerror("Connexion", "Email introuvable.")
        3) Comparer le mot de passe entré avec celui récupéré
           - si différent: messagebox.showerror("Connexion", "Mot de passe incorrect.")
        4) Si OK: ouvrir une Toplevel avec le message
           "Bienvenue dans votre espace de travail !"

        """

    def ouvrir_espace_inscription(self):
        # Masquer la fenêtre principale (login)
        self.withdraw()

        self.win_inscription = tk.Toplevel(self)
        self.win_inscription.title("Inscription")
        self.win_inscription.geometry("520x420")
        self.win_inscription.columnconfigure(0, weight=1)

        # formulaire d'inscription
        form = ttk.LabelFrame(self.win_inscription, text="Créer un compte", padding=12)
        form.grid(row=0, column=0, padx=12, pady=12, sticky="nsew")

        form.columnconfigure(0, weight=0)
        form.columnconfigure(1, weight=1)
        form.columnconfigure(2, weight=0)

        # Prénom
        ttk.Label(form, text="Prénom :").grid(row=0, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_first = ttk.Entry(form)
        self.ent_first.grid(row=0, column=1, padx=0, pady=6, sticky="ew")

        # Nom
        ttk.Label(form, text="Nom :").grid(row=1, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_last = ttk.Entry(form)
        self.ent_last.grid(row=1, column=1, padx=0, pady=6, sticky="ew")

        # Email
        ttk.Label(form, text="Email :").grid(row=2, column=0, padx=(6, 8), pady=6, sticky="e")
        self.signup_email = ttk.Entry(form)
        self.signup_email.grid(row=2, column=1, padx=0, pady=6, sticky="ew")

        # Mot de passe
        ttk.Label(form, text="Mot de passe :").grid(row=3, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_pwd = ttk.Entry(form, show="*")
        self.ent_pwd.grid(row=3, column=1, padx=0, pady=6, sticky="ew")
        ttk.Label(form, text="min. 8 caractères", foreground="#888").grid(row=3, column=2, padx=6, pady=6, sticky="w")

        # Confirmation
        ttk.Label(form, text="Confirmer :").grid(row=4, column=0, padx=(6, 8), pady=6, sticky="e")
        self.ent_pwd2 = ttk.Entry(form, show="*")
        self.ent_pwd2.grid(row=4, column=1, padx=0, pady=6, sticky="ew")

        #  Conditions
        chk_var = tk.BooleanVar(value=False)
        chk = ttk.Checkbutton(form, text="J'accepte les conditions d'utilisation", variable=chk_var)
        chk.grid(row=5, column=0, columnspan=3, padx=6, pady=(8, 2), sticky="w")

        # boutons
        btns = ttk.Frame(self.win_inscription, padding=(12, 0))
        btns.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 12))
        btns.columnconfigure(0, weight=1)
        btns.columnconfigure(1, weight=1)

        btn_retour = ttk.Button(btns, text="Retour", command=self.retour_connexion)
        btn_creer = ttk.Button(btns, text="Créer le compte", command=self.creer_member)

        btn_retour.grid(row=0, column=0, padx=(0, 8), pady=4, sticky="e")
        btn_creer.grid(row=0, column=1, padx=0, pady=4, sticky="w")

    def retour_connexion(self):
        self.deiconify()  # Ré-affiche la fenêtre principale (celle qui avait été cachée par withdraw()).
        self.win_inscription.destroy()

    def creer_member(self):
        prenom = self.ent_first.get()
        nom = self.ent_last.get()
        email = self.signup_email.get()
        mdp = self.ent_pwd.get()
        mdp_confirme = self.ent_pwd2.get()

        if prenom =="" or nom =="" or email =="" or mdp =="" or mdp_confirme=="":
            messagebox.showwarning("Champs requis", "Complétez tous les champs.")

        elif len(mdp) < 8:
            messagebox.showwarning("Mot de passe", "Au moins 8 caractères.")

        elif mdp != mdp_confirme:
            messagebox.showwarning("Mot de passe", "Les mots de passe ne correspondent pas.")

        try:
            self._insert(nom, prenom, email, mdp)
            messagebox.showinfo("Inscription", "Compte crée avec succès")

            self.ent_first.delete(0, "end")
            self.ent_last.delete(0, "end")
            self.signup_email.delete(0, "end")
            self.ent_pwd.delete(0, "end")
            self.ent_pwd2.delete(0, "end")
        except None:
            messagebox.showerror("Inscription", "Erreur lors de la création du compte")

        """
        TODO: insérer les données du formulaire d'inscription dans la base.
        Étapes attendues:
        1) Vérifications UI:
           - champs vides -> showwarning("Champs requis", "Complétez tous les champs.")
           - longueur mdp < 8 -> showwarning("Mot de passe", "Au moins 8 caractères.")
           - mdp != mdp2 -> showwarning("Mot de passe", "Les mots de passe ne correspondent pas.")
        2) Insertion des données

        3) En cas de succès:
           - showinfo("Inscription", "Compte créé avec succès")
           - vider les champs (delete(0, "end")) et remettre le focus sur le premier champ
        """


if __name__ == "__main__":
    App().mainloop()
