import tkinter as tk
import subprocess
from PIL import Image, ImageTk
import webbrowser

class EditarPerfil(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.title("ALL-IN V1.0 - Editar Perfil")
        self.geometry("640x600")
        self.configure(bg="#f0f0f0")
        self.iconbitmap("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.ico")

        # Frame principal (contendrá todo el contenido menos el footer)
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        # Barra de navegación (navbar)
        self.navbar = tk.Frame(self.main_frame, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        self.crear_navbar()

        # Título de la ventana
        encabezado = tk.Label(self.main_frame, text="EDITAR PERFIL", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))

        # Área del perfil
        self.area_perfil = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.area_perfil.pack(pady=20)

        # Cargar imagen del usuario en la celda (0,0)
        self.cargar_imagen_usuario()

        # Crear los menús de selección en un frame (celda (0,1))
        self.cualidades = ["Habilidad técnica", "Creatividad", "Liderazgo", "Comunicación", "Trabajo en equipo"]
        self.crear_cualidades()

        # Botón para guardar cambios (colocado debajo del área de perfil)
        self.boton_guardar = tk.Button(self.main_frame, text="Guardar cambios", command=self.guardar_cambios)
        self.boton_guardar.pack(pady=(10, 20))

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

    # Método para manejar eventos de los botones
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

    # Método para cerrar y abrir otra ventana después de 1 segundo
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

    # Método para cargar la imagen del usuario
    def cargar_imagen_usuario(self):
        imagen_usuario = self.cargar_imagen("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/user.png", (150, 150))
        if imagen_usuario:
            etiqueta_imagen_usuario = tk.Label(self.area_perfil, image=imagen_usuario, bg="#f0f0f0")
            etiqueta_imagen_usuario.image = imagen_usuario
            etiqueta_imagen_usuario.grid(row=0, column=0, padx=30, pady=20)

    # Método para crear los menús desplegables de cualidades
    def crear_cualidades(self):
        self.selecciones = []
        # Creamos un frame para agrupar los menús y lo colocamos en la fila 0, columna 1
        frame_menu = tk.Frame(self.area_perfil, bg="#f0f0f0")
        frame_menu.grid(row=0, column=1, padx=10, pady=20, sticky="n")
        for i, cualidad in enumerate(self.cualidades):
            menu = tk.StringVar(self)
            menu.set("Selecciona una opción")
            desplegable = tk.OptionMenu(frame_menu, menu, "Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5",
                                        "Opción 6", "Opción 7", "Opción 8", "Opción 9", "Opción 10")
            desplegable.pack(pady=5, padx=10, fill="x")
            self.selecciones.append(menu)

    # Método para guardar los cambios
    def guardar_cambios(self):
        seleccionadas = [menu.get() for menu in self.selecciones]
        print("Cambios guardados:", seleccionadas)
        tk.messagebox.showinfo("Guardar", "Cambios guardados exitosamente.")

if __name__ == "__main__":
    app = EditarPerfil()
    app.mainloop()
