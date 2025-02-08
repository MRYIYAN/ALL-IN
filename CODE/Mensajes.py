# Boceto de Mensajes.py
import tkinter as tk

class Mensajes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mensajes")
        self.geometry("400x300")
        tk.Label(self, text="Mensajes", font=("Arial", 16)).pack(pady=20)

if __name__ == "__main__":
    app = Mensajes()
    app.mainloop()
