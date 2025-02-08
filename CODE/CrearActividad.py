import tkinter as tk
import subprocess
from PIL import Image, ImageTk
import webbrowser

class CrearActividad(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.title("ALL-IN V1.0 - Crear Actividad")
        self.geometry("640x600")
        self.configure(bg="#f0f0f0")
        self.iconbitmap("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.ico")

        # Barra de navegación (navbar)
        self.navbar = tk.Frame(self, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        self.crear_navbar()

        # Título de la ventana
        encabezado = tk.Label(self, text="CREAR UNA ACTIVIDAD", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))

        # Área de actividades (puedes agregar botones o listas de actividades aquí)
        self.area_actividades = tk.Frame(self, bg="#f0f0f0")
        self.area_actividades.pack(pady=10)

        # Pie de página (footer)
        self.footer = tk.Frame(self, bg="#FFA500", height=50)
        self.footer.pack(fill="x", side="bottom", pady=0)

        # Redes sociales (izquierda)
        self.iconos_redes = tk.Frame(self.footer, bg="#FFA500")
        self.iconos_redes.pack(side="left", padx=10, pady=5)
        self.cargar_iconos_redes()

        # Enlace (derecha)
        enlace_web = tk.Label(self.footer, text="Visita nuestra web", fg="white", bg="#FFA500", cursor="hand2", font=("Arial", 10, "underline"))
        enlace_web.pack(side="right", padx=10, pady=5)
        enlace_web.bind("<Button-1>", lambda e: self.abrir_pagina("https://tupagina.com"))

        # Botón para navegar a otra pantalla, por ejemplo, "Inicio"
        self.boton_inicio = tk.Button(self, text="Ir al inicio", command=lambda: self.cerrar_y_abrir("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/home.py"))
        self.boton_inicio.pack(pady=20)

    # Método para crear la barra de navegación
    def crear_navbar(self):
        imagen_allin = self.cargar_imagen("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.png", (50, 50))
        if imagen_allin:
            etiqueta_imagen = tk.Label(self.navbar, image=imagen_allin, bg="#333333")
            etiqueta_imagen.image = imagen_allin
            etiqueta_imagen.grid(row=0, column=0, padx=10, pady=10)
        self.crear_boton("Inicio", 1)
        self.crear_boton_desplegable("Perfil", 2, ["Editar perfil"])
        self.crear_boton_desplegable("Actividades", 3, ["Unirse a actividad", "Crear actividad"])
        self.crear_boton("Mapa", 4)
        self.crear_boton("Mensajes", 5)

    # Método para crear botones de la navbar
    def crear_boton(self, texto, columna):
        boton = tk.Button(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat",
                          command=lambda: self.al_hacer_clic(texto))
        boton.grid(row=0, column=columna, padx=20, pady=10)

    # Método para crear botones desplegables en la navbar
    def crear_boton_desplegable(self, texto, columna, opciones):
        desplegable = tk.Menubutton(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat")
        menu = tk.Menu(desplegable, tearoff=0, bg="#333333", fg="white")
        for opcion in opciones:
            menu.add_command(label=opcion, command=lambda opt=opcion: self.al_hacer_clic(opt))
        desplegable.config(menu=menu)
        desplegable.grid(row=0, column=columna, padx=20, pady=10)

    # Método para manejar eventos de los botones (se usa cerrar_y_abrir)
    def al_hacer_clic(self, texto_boton):
        rutas = {
            "Inicio": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/home.py",
            "Editar perfil": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/EditarPerfil.py",
            "Unirse a actividad": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/UnirseActividad.py",
            "Crear actividad": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/CrearActividad.py",
            "Mapa": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/Mapa.py",
            "Mensajes": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/Mensajes.py"
        }
        if texto_boton in rutas:
            self.cerrar_y_abrir(rutas[texto_boton])
        else:
            tk.messagebox.showinfo(texto_boton, f"Has hecho clic en '{texto_boton}'.")

    # Método para cargar los iconos de redes sociales
    def cargar_iconos_redes(self):
        iconos = ["facebook.png", "twitter.png", "instagram.png"]
        for icono in iconos:
            img = self.cargar_imagen(f"C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/{icono}", (25, 25))
            if img:
                etiqueta = tk.Label(self.iconos_redes, image=img, bg="#FFA500")
                etiqueta.image = img
                etiqueta.pack(side="left", padx=5)

    # Método para abrir una página web en el navegador
    def abrir_pagina(self, url):
        webbrowser.open(url)

    # Método para cerrar la ventana actual y abrir otra después de 1 segundo
    def cerrar_y_abrir(self, ruta):
        def accion():
            subprocess.Popen(["python", ruta], shell=True)
            self.destroy()
        self.after(1000, accion)

    # Método para cargar imágenes con manejo de errores
    def cargar_imagen(self, ruta, tamaño):
        try:
            imagen = Image.open(ruta)
            imagen = imagen.convert("RGB")
            imagen = imagen.resize(tamaño, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"Error cargando la imagen {ruta}: {e}")
            return None

if __name__ == "__main__":
    app = CrearActividad()
    app.mainloop()
