# -------------------------------------------------------------------------------#
# Importación de librerías necesarias
# -------------------------------------------------------------------------------
import tkinter as tk
import tkintermapview # pip install tkintermapview
import subprocess # pip install tkintermapview
import webbrowser
from tkinter import messagebox 
from PIL import Image, ImageTk
import os

class Mapa(tk.Tk):
    def __init__(self):
        super().__init__()
        #-------------------------------------------------------------------------------
        # Configuración de la ventana
        #-------------------------------------------------------------------------------
        self.title("ALL-IN V1.0 - Mapa de Actividades")
        self.geometry("640x600")
        self.configure(bg="#f0f0f0")
        self.iconbitmap(os.path.join(os.path.dirname(__file__), "assets/allin.ico"))

        #-------------------------------------------------------------------------------
        # Barra de navegación (navbar)
        #-------------------------------------------------------------------------------
        self.navbar = tk.Frame(self, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        self.crear_navbar()

        #-------------------------------------------------------------------------------
        # Título de la ventana
        #-------------------------------------------------------------------------------
        encabezado = tk.Label(self, text="MAPA DE ACTIVIDADES", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))

        #-------------------------------------------------------------------------------
        # Contenido de la ventana (mapa de actividades)
        #-------------------------------------------------------------------------------
        self.mostrar_mapa()

        #-------------------------------------------------------------------------------
        # Pie de página (footer)
        #-------------------------------------------------------------------------------
        self.footer = tk.Frame(self, bg="#FFA500", height=50)
        self.footer.pack(fill="x", side="bottom", pady=0)

        # Redes sociales (izquierda)
        self.iconos_redes = tk.Frame(self.footer, bg="#FFA500")
        self.iconos_redes.pack(side="left", padx=10, pady=5)
        self.cargar_iconos_redes()

        # Enlace (derecha)
        enlace_web = tk.Label(self.footer, text="Visita nuestra web", fg="white", bg="#FFA500", cursor="hand2", font=("Arial", 10, "underline"))
        enlace_web.pack(side="right", padx=10, pady=5)
        enlace_web.bind("<Button-1>", lambda e: self.abrir_pagina("https://dev-h3ctor23.github.io/"))

    #-------------------------------------------------------------------------------
    # Método para crear la barra de navegación
    #-------------------------------------------------------------------------------
    def crear_navbar(self):
        imagen_allin = self.cargar_imagen(os.path.join(os.path.dirname(__file__), "assets/allin.png"), (50, 50))
        if imagen_allin:
            etiqueta_imagen = tk.Label(self.navbar, image=imagen_allin, bg="#333333")
            etiqueta_imagen.image = imagen_allin
            etiqueta_imagen.grid(row=0, column=0, padx=10, pady=10)
        self.crear_boton("Inicio", 1)
        self.crear_boton_desplegable("Perfil", 2, ["Editar perfil"])
        self.crear_boton_desplegable("Actividades", 3, ["Unirse a actividad", "Crear actividad"])
        self.crear_boton("Mapa", 4)
        self.crear_boton("Mensajes", 5)

    #-------------------------------------------------------------------------------
    # Método para crear botones de la navbar
    #-------------------------------------------------------------------------------
    def crear_boton(self, texto, columna):
        boton = tk.Button(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat", command=lambda: self.al_hacer_clic(texto))
        boton.grid(row=0, column=columna, padx=20, pady=10)

    #-------------------------------------------------------------------------------
    # Método para crear botones desplegables en la navbar
    #-------------------------------------------------------------------------------
    def crear_boton_desplegable(self, texto, columna, opciones):
        desplegable = tk.Menubutton(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat")
        menu = tk.Menu(desplegable, tearoff=0, bg="#333333", fg="white")
        for opcion in opciones:
            menu.add_command(label=opcion, command=lambda opt=opcion: self.al_hacer_clic(opt))
        desplegable.config(menu=menu)
        desplegable.grid(row=0, column=columna, padx=20, pady=10)

    #-------------------------------------------------------------------------------
    # Método para manejar eventos de los botones de la navbar
    #-------------------------------------------------------------------------------
    def al_hacer_clic(self, texto_boton):
        rutas = {
            "Inicio": os.path.join(os.path.dirname(__file__), "home.py"),
            "Editar perfil": os.path.join(os.path.dirname(__file__), "EditarPerfil.py"),
            "Unirse a actividad": os.path.join(os.path.dirname(__file__), "UnirseActividad.py"),
            "Crear actividad": os.path.join(os.path.dirname(__file__), "CrearActividad.py"),
            "Mapa": os.path.join(os.path.dirname(__file__), "Mapa.py"),
            "Mensajes": os.path.join(os.path.dirname(__file__), "Mensajes.py")
        }
        if texto_boton in rutas:
            self.cerrar_y_abrir(rutas[texto_boton])
        else:
            tk.messagebox.showinfo(texto_boton, f"Has hecho clic en '{texto_boton}'.")

    #-------------------------------------------------------------------------------
    # Método para cerrar y abrir otra ventana
    #-------------------------------------------------------------------------------
    def cerrar_y_abrir(self, ruta):
        self.destroy()
        subprocess.Popen(["python", ruta], shell=True)

    #-------------------------------------------------------------------------------
    # Método para mostrar el mapa de actividades
    #-------------------------------------------------------------------------------
    def mostrar_mapa(self):
        # Crear el marco para el mapa
        mapa_frame = tk.Frame(self)
        mapa_frame.pack(pady=10)

        # Crear el widget del mapa
        map_widget = tkintermapview.TkinterMapView(mapa_frame, width=600, height=400)
        map_widget.pack()

        # Establecer la ubicación inicial del mapa (Madrid, España)
        map_widget.set_address("Madrid, España")

        # Agregar un marcador en el mapa en la ubicación de Madrid
        map_widget.set_marker(40.4168, -3.7038)

    #-------------------------------------------------------------------------------
    # Método para cargar los iconos de redes sociales
    #-------------------------------------------------------------------------------
    def cargar_iconos_redes(self):
        iconos = ["facebook.png", "twitter.png", "instagram.png"]
        for icono in iconos:
            img = self.cargar_imagen(os.path.join(os.path.dirname(__file__), f"assets/{icono}"), (25, 25))
            if img:
                etiqueta = tk.Label(self.iconos_redes, image=img, bg="#FFA500")
                etiqueta.image = img
                etiqueta.pack(side="left", padx=5)

    #-------------------------------------------------------------------------------
    # Método para abrir una página web en el navegador
    #-------------------------------------------------------------------------------
    def abrir_pagina(self, url):
        webbrowser.open(url)

    #-------------------------------------------------------------------------------
    # Método para cargar imágenes con manejo de errores
    #-------------------------------------------------------------------------------
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
    app = Mapa()
    app.mainloop()