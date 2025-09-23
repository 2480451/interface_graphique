import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice")
        self.geometry("300x200")
        self.creerwidget()

    def creerwidget(self):
        frm_conteneur = tk.Frame(self, padx=10, pady=10)
        frm_conteneur.pack(fill="both", expand=True)

        # Entrées
        tk.Label(frm_conteneur, text="Nombre 1:").pack()
        self.entry_n1 = tk.Entry(frm_conteneur)
        self.entry_n1.pack(fill="x", padx=5, pady=5)

        tk.Label(frm_conteneur, text="Nombre 2:").pack()
        self.entry_n2 = tk.Entry(frm_conteneur)
        self.entry_n2.pack(fill="x", padx=5, pady=5)

        # Bouton
        bouton_calcul = tk.Button(frm_conteneur, text="Calculer", command=self.calculer)
        bouton_calcul.pack(pady=10)

    def calculer(self):
        try:
            n1 = float(self.entry_n1.get())
            n2 = float(self.entry_n2.get())
            resultat = n1 + n2
            messagebox.showinfo("Résultat", f"La somme est : {resultat}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")


#if __name__ == "__main__":
    #Calculatrice().mainloop()

# main.py
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ma Calculatrice")
        self.resizable(False, False)
        self._build_ui()

    def _build_ui(self):
        self.entry = tk.Entry(self, font=("Helvetica", 20), bd=5, relief="sunken", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")
        buttons = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
            ('0',4,0),('.',4,1),('=',4,2),('+',4,3),
        ]
        for (txt,row,col) in buttons:
            btn = tk.Button(self, text=txt, font=("Helvetica",18), width=4, height=1,
                            command=lambda t=txt: self.on_button(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Clear and Quit
        clr = tk.Button(self, text="C", font=("Helvetica",14), width=10, command=self.clear)
        clr.grid(row=5, column=0, columnspan=2, pady=(0,10))
        q = tk.Button(self, text="Quitter", font=("Helvetica",14), width=10, command=self.destroy)
        q.grid(row=5, column=2, columnspan=2, pady=(0,10))

    def on_button(self, char):
        if char == "=":
            try:
                expr = self.entry.get()
                # evaluation sécurisée minimale : limiter les caractères autorisés
                allowed = "0123456789.+-*/() "
                if any(c not in allowed for c in expr):
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Erreur")
                    return
                result = eval(expr)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Erreur")
        else:
            self.entry.insert(tk.END, char)

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
