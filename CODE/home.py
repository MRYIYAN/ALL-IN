#-------------------------------------------------------------------------------#
# Imports necesarios para la funcionalidad de la ventana Home
#-------------------------------------------------------------------------------#
import tkinter as tk
import subprocess  # Para abrir otros archivos Python
from tkinter import messagebox
from PIL import Image, ImageTk  # Para cargar y mostrar imágenes
import webbrowser  # Para abrir URLs en el navegador
import os  # Para trabajar con el sistema de archivos

#-------------------------------------------------------------------------------#
# Clase principal para la ventana Home
#-------------------------------------------------------------------------------#
class HomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #-------------------------------------------------------------------------------#
        # Configuración de la ventana
        #-------------------------------------------------------------------------------#
        self.title("ALL-IN V1.0 - Inicio")  # Título de la ventana
        self.geometry("640x600")  # Tamaño de la ventana
        self.configure(bg="#f0f0f0")  # Color de fondo de la ventana
        self.iconbitmap("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.ico")  # Ícono de la ventana
        
        #-------------------------------------------------------------------------------#
        # Barra de navegación (navbar)
        #-------------------------------------------------------------------------------#
        self.navbar = tk.Frame(self, bg="#333333")  # Creamos el frame para la barra
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)  # Empacamos la barra en la parte superior
        self.crear_navbar()  # Llamamos al método que crea los botones de la navbar

        #-------------------------------------------------------------------------------#
        # Encabezado
        #-------------------------------------------------------------------------------#
        encabezado = tk.Label(self, text="TUS ACTIVIDADES", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))  # Empacamos el encabezado con un margen superior e inferior

        #-------------------------------------------------------------------------------#
        # Área de actividades
        #-------------------------------------------------------------------------------#
        self.area_actividades = tk.Frame(self, bg="#f0f0f0")  # Frame donde se mostrarán las actividades
        self.area_actividades.pack(pady=10)  # Empacamos el área de actividades con un margen

        # Si existen actividades guardadas, se cargan; de lo contrario se usan los predeterminados
        actividades_guardadas = self.cargar_actividades_guardadas()  # Cargar las actividades guardadas
        if actividades_guardadas:
            self.actividades = actividades_guardadas  # Si hay actividades guardadas, usarlas
        else:
            self.actividades = ["Basketball", "Soccer", "Tennis", "Running", "Swimming", "Cycling"]  # Si no, usar estas actividades predeterminadas
        self.mostrar_actividades()  # Mostrar las actividades

        #-------------------------------------------------------------------------------#
        # Pie de página (footer)
        #-------------------------------------------------------------------------------#
        self.footer = tk.Frame(self, bg="#FFA500", height=50)  # Creamos el pie de página
        self.footer.pack(fill="x", side="bottom", pady=0)  # Empacamos el pie de página en la parte inferior

        # Redes sociales (izquierda)
        self.iconos_redes = tk.Frame(self.footer, bg="#FFA500")  # Creamos un frame para los iconos de redes sociales
        self.iconos_redes.pack(side="left", padx=10, pady=5)  # Empacamos los iconos a la izquierda
        self.cargar_iconos_redes()  # Cargamos los iconos de redes sociales

        # Enlace (derecha)
        enlace_web = tk.Label(self.footer, text="Visita nuestra web", fg="white", bg="#FFA500", cursor="hand2", font=("Arial", 10, "underline"))
        enlace_web.pack(side="right", padx=10, pady=5)  # Empacamos el enlace en la parte derecha
        enlace_web.bind("<Button-1>", lambda e: self.abrir_pagina("https://tupagina.com"))  # Al hacer clic, abrir la página web

    #-------------------------------------------------------------------------------#
    # Método para crear la barra de navegación 
    #-------------------------------------------------------------------------------#
    def crear_navbar(self):
        imagen_allin = self.cargar_imagen("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.png", (50, 50))  # Cargamos la imagen del logo
        if imagen_allin:
            etiqueta_imagen = tk.Label(self.navbar, image=imagen_allin, bg="#333333")  # Mostramos la imagen en la navbar
            etiqueta_imagen.image = imagen_allin  # Guardamos la referencia de la imagen
            etiqueta_imagen.grid(row=0, column=0, padx=10, pady=10)  # Posicionamos la imagen en la barra
        self.crear_boton("Inicio", 1)  # Botón para la página de inicio
        self.crear_boton_desplegable("Perfil", 2, ["Editar perfil"])  # Botón desplegable para perfil
        self.crear_boton_desplegable("Actividades", 3, ["Unirse a actividad", "Crear actividad"])  # Botón desplegable para actividades
        self.crear_boton("Mapa", 4)  # Botón para el mapa
        self.crear_boton("Mensajes", 5)  # Botón para mensajes

    #-------------------------------------------------------------------------------#
    # Método para crear botones de la navbar
    #-------------------------------------------------------------------------------#
    def crear_boton(self, texto, columna):
        boton = tk.Button(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat", command=lambda: self.al_hacer_clic(texto))
        boton.grid(row=0, column=columna, padx=20, pady=10)  # Posicionamos el botón en la barra de navegación

    #-------------------------------------------------------------------------------#
    # Método para crear botones desplegables en la navbar
    #-------------------------------------------------------------------------------#
    def crear_boton_desplegable(self, texto, columna, opciones):
        desplegable = tk.Menubutton(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat")
        menu = tk.Menu(desplegable, tearoff=0, bg="#333333", fg="white")  # Menú de opciones
        for opcion in opciones:
            menu.add_command(label=opcion, command=lambda opt=opcion: self.al_hacer_clic(opt))  # Cada opción en el menú
        desplegable.config(menu=menu)
        desplegable.grid(row=0, column=columna, padx=20, pady=10)  # Posicionamos el desplegable en la barra

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
            self.cerrar_y_abrir(rutas[texto_boton])  # Si el texto del botón coincide con alguna ruta, abrimos el archivo correspondiente
        else:
            messagebox.showinfo(texto_boton, f"Has hecho clic en '{texto_boton}'.")  # Si no, mostramos un mensaje informativo

    #-------------------------------------------------------------------------------#
    # Método para cerrar y abrir otra ventana
    #-------------------------------------------------------------------------------#
    def cerrar_y_abrir(self, ruta):
        self.quit()  # Cerramos la ventana actual
        subprocess.Popen(["python", ruta], shell=True)  # Ejecutamos el nuevo archivo Python

    #-------------------------------------------------------------------------------#
    # Método para mostrar la lista de actividades
    #-------------------------------------------------------------------------------#
    def mostrar_actividades(self):
        for actividad in self.actividades:
            tk.Label(self.area_actividades, text=actividad, font=("Arial", 12), bg="#f0f0f0", fg="#333333").pack(pady=3)  # Empacamos cada actividad en el área correspondiente

    #-------------------------------------------------------------------------------#
    # Método para cargar los iconos de redes sociales
    #-------------------------------------------------------------------------------#
    def cargar_iconos_redes(self):
        iconos = ["facebook.png", "twitter.png", "instagram.png"]  # Lista de iconos de redes sociales
        for icono in iconos:
            img = self.cargar_imagen(f"C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/{icono}", (25, 25))  # Cargamos la imagen de cada icono
            if img:
                etiqueta = tk.Label(self.iconos_redes, image=img, bg="#FFA500")  # Mostramos el icono
                etiqueta.image = img  # Guardamos la referencia de la imagen
                etiqueta.pack(side="left", padx=5)  # Posicionamos los iconos a la izquierda

    #-------------------------------------------------------------------------------#
    # Método para abrir una página web en el navegador
    #-------------------------------------------------------------------------------#
    def abrir_pagina(self, url):
        webbrowser.open(url)  # Abre la URL en el navegador predeterminado

    #-------------------------------------------------------------------------------#
    # Método para cargar imágenes con manejo de errores
    #-------------------------------------------------------------------------------#
    def cargar_imagen(self, ruta, tamaño):
        try:
            imagen = Image.open(ruta)  # Intentamos abrir la imagen
            imagen = imagen.convert("RGB")  # Convertimos la imagen a formato RGB
            imagen = imagen.resize(tamaño, Image.Resampling.LANCZOS)  # Redimensionamos la imagen
            return ImageTk.PhotoImage(imagen)  # Retornamos la imagen lista para ser usada
        except Exception as e:
            print(f"Error cargando la imagen {ruta}: {e}")  # Si hay un error, lo mostramos
            return None  # Si ocurre un error, retornamos None

    #-------------------------------------------------------------------------------#
    # Método para cargar las actividades guardadas (si existen)
    #-------------------------------------------------------------------------------#
    def cargar_actividades_guardadas(self):
        ruta = "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/actividades_guardadas.txt"  # Ruta del archivo de actividades guardadas
        if os.path.exists(ruta):  # Si el archivo existe
            with open(ruta, "r") as f:
                lineas = [linea.strip() for linea in f if linea.strip() != '']  # Leemos las líneas y eliminamos las vacías
            return lineas  # Retornamos las actividades guardadas
        return None  # Si no existe el archivo, retornamos None

if __name__ == "__main__":  # Ejecutamos la aplicación solo si este script es el principal
    app = HomeApp()  # Creamos una instancia de la clase HomeApp
    app.mainloop()  # Ejecutamos el bucle principal de la interfaz gráfica