# interface 1
# gestionnaire de tâches

import tkinter as tk

class GestionnaireTache(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionnaire de Tâches")
        self.geometry("500x800")
        self.header()

    def header(self):
        frm = tk.Frame(self, bg="black")
        frm.pack(side="top", fill="x")

        lbl = tk.Label(frm, text="Ma TO-DO list", font=("Arial", 24, "bold"), fg="Black")
        lbl.pack(side="top", fill="x")


if __name__ == "__main__":
    GestionnaireTache().mainloop()
