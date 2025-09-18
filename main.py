# interface 1
# gestionnaire de tâches

import tkinter as tk

class GestionnaireTache(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de Tâches")
        self.geometry("500x800")
        self.header()
        self.to_do_entry()
        self.add_tache()
        self.list_tache()
        self.tous_prioritaires()
        self.perso_pro()
        self.note_titre()
        self.zone_texte()


    def header(self):
        frm = tk.Frame(self, bg="black")
        frm.pack(side="top", fill="x")

        lbl = tk.Label(frm, text="Ma TO-DO list", font=("Arial", 24, "bold"), fg="Black")
        lbl.pack(side="top", fill="x")


    def to_do_entry(self):
        frm = tk.Frame(self)
        frm.pack(side="top", fill="x")

        entry = tk.Entry(frm, font=("Roboto", 12, "italic"))
        entry.pack(side="top", fill="x", padx=64, pady=24)

    def add_tache(self):
        frm = tk.Frame(self)
        frm.pack(side="top", fill="x")

        btn = tk.Button(frm, text="Ajouter la tâche")
        btn.pack()

    def list_tache(self):
        frm = tk.Frame(self)
        frm.pack(side="top", fill="x")

        liste = tk.Listbox(frm, font=("Arial", 12, "bold"))
        liste.pack(side="top", fill="x", padx=24, pady=24)

    def tous_prioritaires(self):
        frm = tk.Frame(self)
        frm.pack(side="top", fill="x")

        btn = tk.Checkbutton(frm, text="Toutes les tâches sont prioritaires")
        btn.pack()

    def perso_pro(self):
        frm = tk.Frame(self)
        frm.pack(side="top", fill="x")

        radio_button = tk.StringVar(value="Perso")
        tk.Radiobutton(frm, text="Personnel", variable=radio_button, value="Perso").pack(side="top")
        tk.Radiobutton(frm, text="Professionnel", variable=radio_button, value="Pro").pack(side="top")

    def note_titre(self):
        frm = tk.Frame(self)
        frm.pack(side="top", fill="x")

        lbl = tk.Label(frm, text="Notes sur la tâche selectionnée :")
        lbl.pack(side="top", fill="x", padx=24)

    def zone_texte(self):
        frm = tk.Frame(self)
        frm.pack(side="top", fill="x")

        text = tk.Text(frm, font=("Arial", 12,))
        text.pack(side="bottom", fill="x", padx=24, pady=24)


class Formulaire(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulaire")
        self.geometry("500x200")
        self.creerwidget()


    def creerwidget(self):
        frm_conteneur = tk.Frame(self, padx=10, pady=24, relief="solid", bd=1)
        frm_conteneur.pack(fill="x", padx=10, pady=10)

        frm_labentry = tk.Frame(frm_conteneur, padx=10, pady=10)
        frm_labentry.pack(side="left", fill="x", padx=10)

        ligne_nom = tk.Frame(frm_labentry, padx=10, pady=10)
        ligne_nom.pack(side="top", fill="x")

        tk.Label(ligne_nom, text = "Nom:").pack(side="left", padx=10)
        tk.Entry(ligne_nom).pack(fill="x", expand=True, side="left")

        ligne_email = tk.Frame(frm_labentry, padx=10, pady=10)
        ligne_email.pack(side="bottom", fill="x")

        tk.Label(ligne_email, text="Email:").pack(side="left", padx=10)
        tk.Entry(ligne_email).pack(fill="x", expand=True, side="left")

        tk.Button(frm_conteneur, text="Valider").pack(side="right", fill="x", padx=5)




if __name__ == "__main__":
    #GestionnaireTache().mainloop()
    Formulaire().mainloop()
