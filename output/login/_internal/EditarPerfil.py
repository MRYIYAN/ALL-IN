#-------------------------------------------------------------------------------#
# Importación de las librerías necesarias para el funcionamiento de la ventana
#-------------------------------------------------------------------------------#
import tkinter as tk 
import subprocess 
from PIL import Image, ImageTk 
import webbrowser
import tkinter.messagebox as messagebox 
import json 
import os 
#-------------------------------------------------------------------------------#
# Clase principal para la ventana "Editar Perfil"
#-------------------------------------------------------------------------------#
class EditarPerfil(tk.Tk):
    def __init__(self):
        super().__init__()

        #-------------------------------------------------------------------------------#
        # Inicializamos las selecciones guardadas al cargar la ventana
        #-------------------------------------------------------------------------------#
        self.selecciones_guardadas = self.cargar_selecciones_guardadas()

        #-------------------------------------------------------------------------------#
        # Configuración inicial de la ventana principal
        #-------------------------------------------------------------------------------#
        self.title("ALL-IN V1.0 - Editar Perfil")  # Título de la ventana
        self.geometry("640x600")  # Tamaño de la ventana
        self.configure(bg="#f0f0f0")  # Color de fondo de la ventana
        self.iconbitmap(os.path.join(os.path.dirname(__file__), "assets/allin.ico"))  # Ícono de la ventana

        #-------------------------------------------------------------------------------#
        # Frame principal que contendrá todo el contenido menos el footer
        #-------------------------------------------------------------------------------#
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        #-------------------------------------------------------------------------------#
        # Barra de navegación (navbar)
        #-------------------------------------------------------------------------------#
        self.navbar = tk.Frame(self.main_frame, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        self.crear_navbar()

        #-------------------------------------------------------------------------------#
        # Título de la ventana "Editar Perfil"
        #-------------------------------------------------------------------------------#
        encabezado = tk.Label(self.main_frame, text="EDITAR PERFIL", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))

        #-------------------------------------------------------------------------------#
        # Área del perfil, donde se cargará la imagen y se organizarán las opciones
        #-------------------------------------------------------------------------------#
        self.area_perfil = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.area_perfil.pack(pady=20)

        #-------------------------------------------------------------------------------#
        # Cargar la imagen del usuario en la celda (0,0)
        #-------------------------------------------------------------------------------#
        self.cargar_imagen_usuario()

        #-------------------------------------------------------------------------------#
        # Crear los menús de selección de cualidades y habilidades
        #-------------------------------------------------------------------------------#
        self.cualidades = ["Habilidad técnica", "Creatividad", "Liderazgo", "Comunicación", "Trabajo en equipo"]
        self.habilidades = [
            "Boxeo", "Musica Rock", "Musica Jazz", "Gestión de proyectos", "Ciclismo", "Cine", "Viajar",
            "Trabajo en equipo", "Resolución de problemas", "Gastronomía", "Negociación", "Adaptabilidad"
        ]
        self.crear_cualidades()

        #-------------------------------------------------------------------------------#
        # Botón para guardar los cambios realizados en el perfil
        #-------------------------------------------------------------------------------#
        self.boton_guardar = tk.Button(self.main_frame, text="Guardar cambios", command=self.guardar_cambios)
        self.boton_guardar.pack(pady=(10, 20))

        #-------------------------------------------------------------------------------#
        # Pie de página (footer) con redes sociales y enlace
        #-------------------------------------------------------------------------------#
        self.footer = tk.Frame(self, bg="#FFA500", height=50)
        self.footer.pack(fill="x", side="bottom", pady=0)

        #-------------------------------------------------------------------------------#
        # Iconos de redes sociales (izquierda en el footer)
        #-------------------------------------------------------------------------------#
        self.iconos_redes = tk.Frame(self.footer, bg="#FFA500")
        self.iconos_redes.pack(side="left", padx=10, pady=5)
        self.cargar_iconos_redes()

        #-------------------------------------------------------------------------------#
        # Enlace a la página web (derecha en el footer)
        #-------------------------------------------------------------------------------#
        enlace_web = tk.Label(self.footer, text="Visita nuestra web", fg="white", bg="#FFA500", cursor="hand2", font=("Arial", 10, "underline"))
        enlace_web.pack(side="right", padx=10, pady=5)
        enlace_web.bind("<Button-1>", lambda e: self.abrir_pagina("https://dev-h3ctor23.github.io/"))

    #-------------------------------------------------------------------------------#
    # Método para crear la barra de navegación
    #-------------------------------------------------------------------------------#
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

    #-------------------------------------------------------------------------------#
    # Método para crear botones simples en la barra de navegación
    #-------------------------------------------------------------------------------#
    def crear_boton(self, texto, columna):
        boton = tk.Button(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat",
                          command=lambda: self.al_hacer_clic(texto))
        boton.grid(row=0, column=columna, padx=20, pady=10)

    #-------------------------------------------------------------------------------#
    # Método para crear botones desplegables en la barra de navegación
    #-------------------------------------------------------------------------------#
    def crear_boton_desplegable(self, texto, columna, opciones):
        desplegable = tk.Menubutton(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat")
        menu = tk.Menu(desplegable, tearoff=0, bg="#333333", fg="white")
        for opcion in opciones:
            menu.add_command(label=opcion, command=lambda opt=opcion: self.al_hacer_clic(opt))
        desplegable.config(menu=menu)
        desplegable.grid(row=0, column=columna, padx=20, pady=10)

    #-------------------------------------------------------------------------------#
    # Acción a realizar cuando se hace clic en un botón de la barra de navegación
    #-------------------------------------------------------------------------------#
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

    #-------------------------------------------------------------------------------#
    # Método para cargar los iconos de las redes sociales en el footer
    #-------------------------------------------------------------------------------#
    def cargar_iconos_redes(self):
        iconos = ["facebook.png", "twitter.png", "instagram.png"]
        for icono in iconos:
            img = self.cargar_imagen(os.path.join(os.path.dirname(__file__), f"assets/{icono}"), (25, 25))
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
    # Método para cerrar la ventana actual y abrir una nueva
    #-------------------------------------------------------------------------------#
    def cerrar_y_abrir(self, ruta):
        def accion():
            subprocess.Popen(["python", ruta], shell=True)
            self.destroy()
        self.after(1000, accion)

    #-------------------------------------------------------------------------------#
    # Método para cargar una imagen con un tamaño específico
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

    #-------------------------------------------------------------------------------#
    # Método para cargar la imagen del usuario en el perfil
    #-------------------------------------------------------------------------------#
    def cargar_imagen_usuario(self):
        imagen_usuario = self.cargar_imagen("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/user1.png", (150, 150))
        imagen_usuario = self.cargar_imagen(os.path.join(os.path.dirname(__file__), "assets/user1.png"), (150, 150))
        if imagen_usuario:
            etiqueta_imagen_usuario = tk.Label(self.area_perfil, image=imagen_usuario, bg="#f0f0f0")
            etiqueta_imagen_usuario.image = imagen_usuario
            etiqueta_imagen_usuario.grid(row=0, column=0, padx=30, pady=20)

    #-------------------------------------------------------------------------------#
    # Método para crear los menús de cualidades y habilidades
    #-------------------------------------------------------------------------------#
    def crear_cualidades(self):
        self.selecciones = []
        frame_menu = tk.Frame(self.area_perfil, bg="#f0f0f0")
        frame_menu.grid(row=0, column=1, padx=10, pady=20, sticky="n")

        for i, cualidad in enumerate(self.cualidades):
            menu = tk.StringVar(self)
            valor_guardado = self.selecciones_guardadas.get(cualidad, "Selecciona una habilidad")
            menu.set(valor_guardado)

            desplegable = tk.OptionMenu(frame_menu, menu, *self.habilidades)
            desplegable.pack(pady=5, padx=10, fill="x")
            self.selecciones.append(menu)

    #-------------------------------------------------------------------------------#
    # Método para guardar los cambios realizados por el usuario
    #-------------------------------------------------------------------------------#
    def guardar_cambios(self):
        for i, cualidad in enumerate(self.cualidades):
            self.selecciones_guardadas[cualidad] = self.selecciones[i].get()

        self.guardar_selecciones_guardadas()

        print("Cambios guardados:", self.selecciones_guardadas)
        tk.messagebox.showinfo("Guardar", "Cambios guardados exitosamente.")

    #-------------------------------------------------------------------------------#
    # Método para guardar las selecciones en un archivo JSON
    #-------------------------------------------------------------------------------#
    def guardar_selecciones_guardadas(self):
        try:
            ruta_guardado = os.path.join(os.path.dirname(__file__), "selecciones_guardadas.json")
            with open(ruta_guardado, "w") as archivo:
                json.dump(self.selecciones_guardadas, archivo)
        except Exception as e:
            print(f"Error al guardar las selecciones: {e}")

    #-------------------------------------------------------------------------------#
    # Método para cargar las selecciones guardadas desde un archivo JSON
    #-------------------------------------------------------------------------------#
    def cargar_selecciones_guardadas(self):
        ruta_guardado = os.path.join(os.path.dirname(__file__), "selecciones_guardadas.json")
        if os.path.exists(ruta_guardado):
            try:
                with open(ruta_guardado, "r") as archivo:
                    return json.load(archivo)
            except Exception as e:
                print(f"Error al cargar las selecciones guardadas: {e}")
        return {}

#-------------------------------------------------------------------------------#
# Ejecutar la aplicación si es el archivo principal
#-------------------------------------------------------------------------------#
if __name__ == "__main__":
    app = EditarPerfil()
    app.mainloop()