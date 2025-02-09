#-------------------------------------------------------------------------------#
# Imports necesarios para la funcionalidad de la ventana
#-------------------------------------------------------------------------------#
import tkinter as tk 
from tkinter import messagebox 
from tkcalendar import Calendar  # instalar la librería tkcalendar para usar el widget de calendario pip install tkcalendar
import subprocess 
from PIL import Image, ImageTk # Instalar la librería PIL pip install pillow
import webbrowser
import os

class CrearActividad(tk.Tk):
    def __init__(self):
        super().__init__()
        #-------------------------------------------------------------------------------#
        # Configuración de la ventana
        #-------------------------------------------------------------------------------#
        self.title("ALL-IN V1.0 - Crear Actividad")
        self.geometry("640x750")  # Aumenté la altura de la ventana
        self.configure(bg="#f0f0f0")
        script_dir = os.path.dirname(__file__)
        icon_path = os.path.join(script_dir, "assets", "allin.ico")
        self.iconbitmap(icon_path)

        #-------------------------------------------------------------------------------#
        # Barra de navegación (navbar)
        #-------------------------------------------------------------------------------#
        self.navbar = tk.Frame(self, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        self.crear_navbar()

        #-------------------------------------------------------------------------------#
        # Título de la ventana
        #-------------------------------------------------------------------------------#
        encabezado = tk.Label(self, text="CREAR UNA ACTIVIDAD", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))

        #-------------------------------------------------------------------------------#
        # Área de actividades (puedes agregar botones o listas de actividades aquí)
        #-------------------------------------------------------------------------------#
        self.area_actividades = tk.Frame(self, bg="#f0f0f0")
        self.area_actividades.pack(pady=10)

        #-------------------------------------------------------------------------------#
        # Ingreso de actividad
        #-------------------------------------------------------------------------------#
        self.actividad_label = tk.Label(self.area_actividades, text="Ingrese el nombre de la actividad:", font=("Arial", 12), bg="#f0f0f0")
        self.actividad_label.pack(pady=5)
        self.actividad_entry = tk.Entry(self.area_actividades, font=("Arial", 12), width=50)
        self.actividad_entry.pack(pady=5)

        #-------------------------------------------------------------------------------#
        # Selección de fecha
        #-------------------------------------------------------------------------------#
        self.fecha_label = tk.Label(self.area_actividades, text="Selecciona la fecha y hora de la actividad:", font=("Arial", 12), bg="#f0f0f0")
        self.fecha_label.pack(pady=5)
        self.calendario = Calendar(self.area_actividades, selectmode='day', date_pattern='y-mm-dd', font=("Arial", 12))
        self.calendario.pack(pady=5)

        #-------------------------------------------------------------------------------#
        # Tipo de actividad
        #-------------------------------------------------------------------------------#
        self.tipo_label = tk.Label(self.area_actividades, text="Selecciona el tipo de actividad:", font=("Arial", 12), bg="#f0f0f0")
        self.tipo_label.pack(pady=5)
        self.tipo_actividad = tk.StringVar()
        self.tipo_menu = tk.OptionMenu(self.area_actividades, self.tipo_actividad, "Deporte", "Cultura", "Social", "Educativo")
        self.tipo_menu.pack(pady=5)

        #-------------------------------------------------------------------------------#
        # Descripción de la actividad
        #-------------------------------------------------------------------------------#
        self.descripcion_label = tk.Label(self.area_actividades, text="Descripción de la actividad:", font=("Arial", 12), bg="#f0f0f0")
        self.descripcion_label.pack(pady=5)
        self.descripcion_text = tk.Text(self.area_actividades, font=("Arial", 12), height=4, width=50)
        self.descripcion_text.pack(pady=5)

        #-------------------------------------------------------------------------------#
        # Botón para enviar evento
        #-------------------------------------------------------------------------------#
        self.boton_enviar = tk.Button(self.area_actividades, text="Enviar Evento", font=("Arial", 12, "bold"), bg="#28a745", command=self.enviar_evento)
        self.boton_enviar.pack(pady=10)

        #-------------------------------------------------------------------------------#
        # Pie de página (footer)
        #-------------------------------------------------------------------------------#
        self.footer = tk.Frame(self, bg="#FFA500", height=50)
        self.footer.pack(fill="x", side="bottom", pady=0)

        #-------------------------------------------------------------------------------#
        # Redes sociales (izquierda)
        #-------------------------------------------------------------------------------#
        self.iconos_redes = tk.Frame(self.footer, bg="#FFA500")
        self.iconos_redes.pack(side="left", padx=10, pady=5)
        self.cargar_iconos_redes()

        #-------------------------------------------------------------------------------#
        # Enlace (derecha)
        #-------------------------------------------------------------------------------#
        enlace_web = tk.Label(self.footer, text="Visita nuestra web", fg="white", bg="#FFA500", cursor="hand2", font=("Arial", 10, "underline"))
        enlace_web.pack(side="right", padx=10, pady=5)
        enlace_web.bind("<Button-1>", lambda e: self.abrir_pagina("https://dev-h3ctor23.github.io/"))

    #-------------------------------------------------------------------------------#
    # Método para enviar el evento
    #-------------------------------------------------------------------------------#
    def enviar_evento(self):
        actividad = self.actividad_entry.get()
        fecha = self.calendario.get_date()
        tipo = self.tipo_actividad.get()
        descripcion = self.descripcion_text.get("1.0", tk.END).strip()

        #-------------------------------------------------------------------------------#
        # Verificación de campos vacíos
        #-------------------------------------------------------------------------------#
        if not actividad or not fecha or not tipo or not descripcion:
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        #-------------------------------------------------------------------------------#
        # Aquí puedes agregar código para guardar el evento en una base de datos o enviarlo a un servidor
        #-------------------------------------------------------------------------------#
        messagebox.showinfo("Evento registrado", "GRACIAS POR CREAR UN EVENTO, Sera enviado hacia los moderadores para ser revisado. 🙂")

        #-------------------------------------------------------------------------------#
        # Limpiar los campos después de enviar
        #-------------------------------------------------------------------------------#
        self.actividad_entry.delete(0, tk.END)
        self.descripcion_text.delete("1.0", tk.END)

    #-------------------------------------------------------------------------------#
    # Método para crear la barra de navegación
    #-------------------------------------------------------------------------------#
    def crear_navbar(self):
        imagen_allin = self.cargar_imagen("assets/allin.png", (50, 50))
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
        boton = tk.Button(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat",
                          command=lambda: self.al_hacer_clic(texto))
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
    # Método para manejar eventos de los botones (se usa cerrar_y_abrir)
    #-------------------------------------------------------------------------------#
    def al_hacer_clic(self, texto_boton):
        rutas = {
            "Inicio": "home.py",
            "Editar perfil": "EditarPerfil.py",
            "Unirse a actividad": "UnirseActividad.py",
            "Crear actividad": "CrearActividad.py",
            "Mapa": "Mapa.py",
            "Mensajes": "Mensajes.py"
        }
        if texto_boton in rutas:
            self.cerrar_y_abrir(rutas[texto_boton])
        else:
            tk.messagebox.showinfo(texto_boton, f"Has hecho clic en '{texto_boton}'.")

    #-------------------------------------------------------------------------------#
    # Método para cargar los iconos de redes sociales
    #-------------------------------------------------------------------------------#
    def cargar_iconos_redes(self):
        iconos = ["facebook.png", "twitter.png", "instagram.png"]
        for icono in iconos:
            img = self.cargar_imagen(f"assets/{icono}", (25, 25))
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
    # Método para cerrar la ventana actual y abrir otra después de 1 segundo
    #-------------------------------------------------------------------------------#
    def cerrar_y_abrir(self, ruta):
        script_dir = os.path.dirname(__file__)
        ruta_completa = os.path.join(script_dir, ruta)  # Construción de la ruta completa
        def accion():
            subprocess.Popen(["python", ruta_completa], shell=True)
            self.destroy()
        self.after(1000, accion)

    #-------------------------------------------------------------------------------#
    # Método para cargar imágenes con manejo de errores
    #-------------------------------------------------------------------------------#
    def cargar_imagen(self, ruta, tamaño):
        script_dir = os.path.dirname(__file__)
        ruta_completa = os.path.join(script_dir, ruta)  # Construyendo la ruta completa
        try:
            imagen = Image.open(ruta_completa)
            imagen = imagen.convert("RGB")
            imagen = imagen.resize(tamaño, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"Error cargando la imagen {ruta_completa}: {e}")
            return None

if __name__ == "__main__":
    app = CrearActividad()
    app.mainloop()