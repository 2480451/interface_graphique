import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

class ApplicationCourbe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Visualisation de courbes scientifiques")
        self.geometry("800x600")

        # Configuration de la grille principale
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        # ---- Paramètres par défaut ----
        self.fonction = tk.StringVar(value="Courbe linéaire")

        # ---- Interface graphique ----
        self.creer_widgets()
        self.creer_plot()

    def creer_widgets(self):
        """Création de la partie interface (contrôles)"""
        frame = ttk.Frame(self)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Rendre les colonnes extensibles si besoin
        for i in range(3):
            frame.columnconfigure(i, weight=1)

        #header
        header= ttk.Label(frame, text="Choisir un type de graphique")
        header.grid(row=0, column=0, sticky="ew", padx= 25, pady=(0,10))
        #inputs
        self.combo = ttk.Combobox(frame, textvariable=self.fonction, values=["Courbe linéaire", "Nuage de points", "Diagramme en barres"], width=10)
        self.combo.grid(row=1, column=0, sticky="ew", padx=25)
        self.combo.current(0)

        # Bouton Tracer
        btn_tracer = ttk.Button(frame, text="Tracer", command=self.tracer_courbe)
        btn_tracer.grid(row=1, column=3, columnspan=2, padx=10, sticky="sn")

    def creer_plot(self):
        """Initialise le graphique Matplotlib"""
        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


    def tracer_courbe(self):
        """Trace la courbe sélectionnée"""
        fct = self.combo.get()
        self.ax.clear()
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        noms = ["Olivier", "Marius", "Gabriel", "Samuel", "Édouard", "Helmi"]
        ages = [18.6, 18.1, 18.05, 18.7, 18.5, 33]

        if fct == "Courbe linéaire":
            self.ax.plot(x, y, label=f"sin(x)", color="blue", linestyle="dashdot")
            self.ax.set_title(f"Courbe linéaire sin(x)")
            self.ax.set_xlabel("X")
            self.ax.set_ylabel("Y")
            self.ax.grid(True)
            self.ax.legend()
            self.canvas.draw()
        elif fct == "Nuage de points":
            self.ax.scatter(x, y, label=f"sin(x)", color="purple")
            self.ax.set_title(f"Courbe linéaire sin(x)")
            self.ax.set_xlabel("X")
            self.ax.set_ylabel("Y")
            self.ax.grid(True)
            self.ax.legend()
            self.canvas.draw()
        elif fct == "Diagramme en barres":
            self.ax.bar(noms, ages, label=f"Diagramme", color="orange")
            self.ax.set_title(f"Diagramme")
            self.ax.set_xlabel("Noms")
            self.ax.set_ylabel("Âges")
            self.ax.grid(True)
            self.ax.legend()
            self.canvas.draw()









# --------- Lancement de l'application ---------
if __name__ == "__main__":
    app = ApplicationCourbe()
    app.mainloop()
