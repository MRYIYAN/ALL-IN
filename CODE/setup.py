#-------------------------------------------------------------------------------#
# Imports necesarios para la funcionalidad del programa.
#-------------------------------------------------------------------------------#

import tkinter as tk

#-------------------------------------------------------------------------------#

# Creamos una nueva ventana con Tkinter.




root = tk.Tk()

root.title("ALL-IN V1.0")

root.geometry("800x600")

label = tk.Label(root, text="Bienvenidos", font=("Helvetica", 16))

label.pack(pady=10)



button = tk.Button(root, text="Presionar", command=lambda: label.config(text="Boton presionado"))

button = tk.Button(root, text="Iniciar", command=lambda: label.config(text="Hola Mundo"))

button = tk.Button(root, text="Salir", command=root.quit)

root.mainloop()

# Output: Hola Mundo

class App(tk.Tk):
    def __init__(self):
        super().__init__()