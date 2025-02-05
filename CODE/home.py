import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Para cargar y mostrar imágenes

#-------------------------------------------------------------------------------#
# Clase principal para la ventana Home
#-------------------------------------------------------------------------------#

class HomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #-------------------------------------------------------------------------------#
        # Configuración de la ventana
        #-------------------------------------------------------------------------------#
        self.title("ALL-IN V1.0 - Home")
        self.geometry("680x600")  
        self.configure(bg="#f0f0f0")
        #-------------------------------------------------------------------------------#
        # Frame para la navbar
        #-------------------------------------------------------------------------------#
        self.navbar = tk.Frame(self, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        #-------------------------------------------------------------------------------#
        # Crear el menú
        #-------------------------------------------------------------------------------#
        self.create_navbar()

        #-------------------------------------------------------------------------------#
        # Cargar el icono de la ventana 
        #-------------------------------------------------------------------------------#
        self.iconbitmap("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.ico")  

#-------------------------------------------------------------------------------#
# Métodos de la clase HomeApp
#-------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------#
    # Crear la barra de navegación
    #-------------------------------------------------------------------------------#
    def create_navbar(self):
        # Cargar la imagen y mostrarla en el lado izquierdo
        allin_image = self.load_image("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.png", (50, 50))  # Ajusta la ruta de la imagen
        if allin_image:
            image_label = tk.Label(self.navbar, image=allin_image, bg="#333333")
            image_label.image = allin_image  # Mantener una referencia a la imagen
            image_label.grid(row=0, column=0, padx=10, pady=10)

        # Crear los botones del navbar
        self.create_button("Home", 1)
        self.create_dropdown_button("Perfil", 2, ["Editar perfil"])
        self.create_dropdown_button("Actividades", 3, ["Unirse a actividad", "Crear actividad"])
        self.create_button("Mapa", 4)
        self.create_button("Mensajes", 5)

    #-------------------------------------------------------------------------------#
    # Cargar una imagen y redimensionarla
    #-------------------------------------------------------------------------------#
    def create_button(self, text, column):
        button = tk.Button(self.navbar, text=text, font=("Arial", 12), fg="white", bg="#333333", relief="flat", command=lambda: self.on_button_click(text))
        button.grid(row=0, column=column, padx=20, pady=10)
    
    #-------------------------------------------------------------------------------#

    #-------------------------------------------------------------------------------#
    # Crear botones con menú desplegable
    #-------------------------------------------------------------------------------#
    def create_dropdown_button(self, text, column, options):
        # Botón con menú desplegable
        dropdown = tk.Menubutton(self.navbar, text=text, font=("Arial", 12), fg="white", bg="#333333", relief="flat")
        menu = tk.Menu(dropdown, tearoff=0, bg="#333333", fg="white")
        
        for option in options:
            menu.add_command(label=option, command=lambda opt=option: self.on_button_click(opt))

        dropdown.config(menu=menu)
        dropdown.grid(row=0, column=column, padx=20, pady=10)
    
    #-------------------------------------------------------------------------------#

    #-------------------------------------------------------------------------------#
    # Evento al hacer clic en un botón
    #-------------------------------------------------------------------------------#
    def on_button_click(self, button_text):
        if button_text == "Perfil":
            messagebox.showinfo("Perfil", "Has hecho clic en 'Editar perfil'.")
        elif button_text == "Home":
            messagebox.showinfo("Home", "Bienvenido a la página de inicio.")
        elif button_text == "Actividades":
            messagebox.showinfo("Actividades", "Elige una opción: Unirte o Crear actividad.")
        elif button_text == "Unirse a actividad":
            messagebox.showinfo("Unirse a actividad", "Aquí podrás unirte a una actividad.")
        elif button_text == "Crear actividad":
            messagebox.showinfo("Crear actividad", "Aquí podrás crear una nueva actividad.")
        elif button_text == "Mapa":
            messagebox.showinfo("Mapa", "El mapa está en construcción.")
        elif button_text == "Mensajes":
            messagebox.showinfo("Mensajes", "Los mensajes están en construcción.")
    #-------------------------------------------------------------------------------#

    #-------------------------------------------------------------------------------#
    # Cargar una imagen y redimensionarla
    #-------------------------------------------------------------------------------#
    def load_image(self, path, size):
        try:
            image = Image.open(path)
            image = image.convert("RGB")  
            image = image.resize(size, Image.Resampling.LANCZOS)  
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error cargando la imagen {path}: {e}")
            return None
    #-------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------#
# Punto de entrada de la aplicación
#-------------------------------------------------------------------------------#

if __name__ == "__main__":
    app = HomeApp()
    app.mainloop()
