#-------------------------------------------------------------------------------#
# Imports necesarios para la funcionalidad de la ventana Unirse a Actividad
#-------------------------------------------------------------------------------#
import tkinter as tk
import subprocess
from PIL import Image, ImageTk
import webbrowser
from tkinter import messagebox

#-------------------------------------------------------------------------------#
# Clase principal para la ventana Unirse a Actividad
#-------------------------------------------------------------------------------#
class UnirseActividad(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.title("ALL-IN V1.0 - Unirse a Actividad")
        self.geometry("640x600")
        self.configure(bg="#f0f0f0")
        self.iconbitmap("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.ico")

        # Barra de navegación (navbar)
        self.navbar = tk.Frame(self, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        self.crear_navbar()

        # Título de la ventana
        encabezado = tk.Label(self, text="UNIRSE A UNA ACTIVIDAD", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))

        # Área de actividades con scrollbar
        self.crear_area_actividades()

        # Variable para almacenar la actividad seleccionada (usada en los radio buttons)
        self.seleccion = tk.StringVar()
        self.seleccion.set("")

        # Lista de actividades (ejemplo con 10 actividades; ajusta las rutas de las imágenes según corresponda)
        self.lista_actividades = [
            {"nombre": "Basketball", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad1.png"},
            {"nombre": "Soccer", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad2.png"},
            {"nombre": "Tennis", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad3.png"},
            {"nombre": "Running", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad4.png"},
            {"nombre": "Swimming", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad5.png"},
            {"nombre": "Cycling", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad6.png"},
            {"nombre": "Yoga", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad7.png"},
            {"nombre": "Boxing", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad8.png"},
            {"nombre": "Baseball", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad9.png"},
            {"nombre": "Volleyball", "imagen": "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/actividad10.png"}
        ]
        self.listar_actividades()

        # Botón para unirse a la actividad
        btn_unirse = tk.Button(self, text="Unirse", font=("Arial", 12, "bold"), bg="#FFA500", fg="white", command=self.unirse)
        btn_unirse.pack(pady=10)

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

    #-------------------------------------------------------------------------------#
    # Método para crear la barra de navegación
    #-------------------------------------------------------------------------------#
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

    #-------------------------------------------------------------------------------#
    # Método para crear botones de la navbar
    #-------------------------------------------------------------------------------#
    def crear_boton(self, texto, columna):
        boton = tk.Button(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat", command=lambda: self.al_hacer_clic(texto))
        boton.grid(row=0, column=columna, padx=20, pady=10)

    #-------------------------------------------------------------------------------#
    # Método para crear botones desplegables en la navbar
    #-------------------------------------------------------------------------------#
    def crear_boton_desplegable(self, texto, columna, opciones):
        desplegable = tk.Menubutton(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat")
        menu = tk.Menu(desplegable, tearoff=0, bg="#333333", fg="white")
        for opcion in opciones:
            menu.add_command(label=opcion, command=lambda opt=opcion: self.al_hacer_clic(opt))
        desplegable.config(menu=menu)
        desplegable.grid(row=0, column=columna, padx=20, pady=10)

    #-------------------------------------------------------------------------------#
    # Método para manejar eventos de los botones de la navbar
    #-------------------------------------------------------------------------------#
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

    #-------------------------------------------------------------------------------#
    # Método para cerrar y abrir otra ventana
    #-------------------------------------------------------------------------------#
    def cerrar_y_abrir(self, ruta):
        self.destroy()
        subprocess.Popen(["python", ruta], shell=True)

    #-------------------------------------------------------------------------------#
    # Método para crear el área de actividades con scrollbar
    #-------------------------------------------------------------------------------#
    def crear_area_actividades(self):
        self.contenedor = tk.Frame(self, bg="#f0f0f0")
        self.contenedor.pack(fill="both", expand=True, padx=10, pady=10)
        self.canvas = tk.Canvas(self.contenedor, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.contenedor, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.frame_actividades = tk.Frame(self.canvas, bg="#f0f0f0")
        self.canvas.create_window((0,0), window=self.frame_actividades, anchor="nw")

    #-------------------------------------------------------------------------------#
    # Método para listar las actividades en forma de banners con radio buttons
    #-------------------------------------------------------------------------------#
    def listar_actividades(self):
        # Si no se ha creado el área de actividades, crearla
        if not hasattr(self, 'frame_actividades'):
            self.crear_area_actividades()
        for actividad in self.lista_actividades:
            banner = tk.Frame(self.frame_actividades, bg="#ffffff", relief="raised", borderwidth=1)
            banner.pack(fill="x", pady=5, padx=5)
            img = self.cargar_imagen(actividad["imagen"], (600, 150))
            if img:
                etiqueta_img = tk.Label(banner, image=img, bg="#ffffff")
                etiqueta_img.image = img
                etiqueta_img.pack(side="top", fill="x")
            etiqueta_nombre = tk.Label(banner, text=actividad["nombre"], font=("Arial", 12, "bold"), bg="#ffffff", fg="#333333")
            etiqueta_nombre.pack(side="top", pady=5)
            rb = tk.Radiobutton(banner, text="Seleccionar", variable=self.seleccion, value=actividad["nombre"], bg="#ffffff", font=("Arial", 10))
            rb.pack(side="bottom", pady=5)

    #-------------------------------------------------------------------------------#
    # Método para unirse a la actividad seleccionada
    #-------------------------------------------------------------------------------#
    def unirse(self):
        actividad_seleccionada = self.seleccion.get()
        if actividad_seleccionada:
            # Guardar la actividad seleccionada (por ejemplo, en un archivo)
            with open("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/actividades_guardadas.txt", "w") as f:
                f.write(actividad_seleccionada + "\n")
            tk.messagebox.showinfo("Unirse", f"Te has unido a {actividad_seleccionada}")
            self.destroy()
            subprocess.Popen(["python", "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/home.py"], shell=True)
        else:
            tk.messagebox.showerror("Error", "No has seleccionado ninguna actividad.")

    #-------------------------------------------------------------------------------#
    # Método para cargar los iconos de redes sociales
    #-------------------------------------------------------------------------------#
    def cargar_iconos_redes(self):
        iconos = ["facebook.png", "twitter.png", "instagram.png"]
        for icono in iconos:
            img = self.cargar_imagen(f"C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/{icono}", (25, 25))
            if img:
                etiqueta = tk.Label(self.iconos_redes, image=img, bg="#FFA500")
                etiqueta.image = img
                etiqueta.pack(side="left", padx=5)

    #-------------------------------------------------------------------------------#
    # Método para abrir una página web en el navegador
    #-------------------------------------------------------------------------------#
    def abrir_pagina(self, url):
        webbrowser.open(url)

    #-------------------------------------------------------------------------------#
    # Método para cargar imágenes con manejo de errores
    #-------------------------------------------------------------------------------#
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
    app = UnirseActividad()
    app.mainloop()
