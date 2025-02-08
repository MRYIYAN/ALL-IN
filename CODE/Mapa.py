# Boceto de Mapa.py
import tkinter as tk

class Mapa(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mapa")
        self.geometry("400x300")
        tk.Label(self, text="Mapa", font=("Arial", 16)).pack(pady=20)

if __name__ == "__main__":
    app = Mapa()
    app.mainloop()