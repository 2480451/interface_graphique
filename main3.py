import tkinter as tk

class FormulaireGrid(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("500x520")

        # conteneur principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        content = tk.Frame(self, pady=10)
        content.grid(row=0, column=0, sticky="ew", padx=5)
        content.columnconfigure(0, weight=0)
        content.columnconfigure(1, weight=1)


        self.titre = tk.Label(content, text="To-Do list", font=("Roboto", 20, "bold"))
        self.titre.grid(row=0, columnspan=2, sticky="ew", padx=5, pady=(4, 10))

        tk.Label(content, text="Taper la tâche à ajouter :").grid(row=2, column=0, sticky="w")
        self.tache = (tk.Entry(content))
        self.tache.grid(row=2, column=1, sticky="ew", pady=8)

        tk.Label(content, text="Durée estimée de la tâche en minutes :").grid(row=3, column=0, sticky="w")
        self.duree = (tk.Entry(content))
        self.duree.grid(row=3, column=1, sticky="ew", pady=8)

        self.prioritaire = tk.BooleanVar(value=False)
        self.cb_prioritaire = (tk.Checkbutton(content, text="Toutes les nouvelles tâches sont prioritaires", variable=self.prioritaire))
        self.cb_prioritaire.grid(row=4, columnspan=2, sticky="w", pady=16)

        tk.Label(content, text="Choisir le type de tâche :").grid(row=5, column=0, sticky="w")

        self.type = tk.StringVar(value="Perso")
        tk.Radiobutton(content, text="Personnel", variable=self.type, value="Perso").grid(row=5, column=1, sticky="w", pady=4)
        tk.Radiobutton(content, text="Professionnel", variable=self.type, value="Pro").grid(row=6, column=1, sticky="w")

        self.ajouter_bouton = (tk.Button(content, text="Ajouter la tâche", state="disabled", command=self.ajouter_tache))
        self.ajouter_bouton.grid(row=7, columnspan=2, padx=96, pady=24)

        self.lb = tk.Listbox(content)
        self.lb.grid(row=8, column=0, columnspan=2, sticky="ew", padx=8, pady=24)

    def ajouter_tache(self):
        tache = self.tache.get()
        duree = self.duree.get()
        type_tache = self.type.get()
        prioritaire = ""
        if self.prioritaire.get():
            prioritaire = "[P]"

        self.lb.insert("end", f"{prioritaire}[{type_tache}][{duree}]{tache}")
        self.tache.delete(0, tk.END)
        self.duree.delete(0, tk.END)


    def valider_duree(self, duree):
        if duree == "" or duree == "-" or duree.startswith("-") or isinstance(duree, str):
            return False

        return True

    def valider_tache(self, *args):
        tache = self.tache.get()
        duree = self.duree.get()

        tache_valide = len(tache) > 0
        duree_valide = len(duree) > 0

        if tache_valide and duree_valide:
            self.ajouter_bouton(state=active)




if __name__ == "__main__":
    FormulaireGrid().mainloop()