import tkinter as tk

class FormulaireGrid(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("400x100")

        # conteneur principal
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        content = tk.Frame(self, pady=10, bd=2, relief="groove")
        content.grid(row=0, column=0, sticky="ew", padx=5)

        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=40)
        content.columnconfigure(2, weight=2)
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)

        tk.Label(content, text="Username :").grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        tk.Label(content, text="Password :").grid(row=1, column=0, sticky="ew", padx=10, pady=5)

        tk.Entry(content).grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        tk.Entry(content, show="*").grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        tk.Button(content, text="Log in").grid(row=0, column=2, rowspan=2, sticky="ew", padx=10, pady=10)

if __name__ == "__main__":
    FormulaireGrid().mainloop()