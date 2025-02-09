#-------------------------------------------------------------------------------#
# Imports necesarios para la funcionalidad del programa
#-------------------------------------------------------------------------------#

import tkinter as tk  # Importa la librería de Tkinter pip install tk
import subprocess  # Para abrir otros archivos Python
import os  # Para manejar rutas de archivos
from PIL import Image, ImageTk  # Importa la librería PIL pip install pillow
from tkinter import messagebox  # Importa la librería para ventanas emergentes

#-------------------------------------------------------------------------------#
# Clase principal de la aplicación de Login
#-------------------------------------------------------------------------------#

class AplicacionLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        #-------------------------------------------------------------------------------#
        # Configuración de la ventana principal.
        #-------------------------------------------------------------------------------#

        self.title("ALL-IN V1.0 - Login")
        self.geometry("525x300")  
        self.configure(bg="#333333")  # Color de fondo de la ventana
        
        #-------------------------------------------------------------------------------#
        # Cargar el icono de la ventana 
        #-------------------------------------------------------------------------------#
        ruta_icono = os.path.join(os.path.dirname(__file__), "assets", "allin.ico")
        self.iconbitmap(ruta_icono)

        #-------------------------------------------------------------------------------#
        # Carga de la imagen de usuario 
        #-------------------------------------------------------------------------------#

        ruta_imagen_usuario = os.path.join(os.path.dirname(__file__), "assets", "user1.png")
        self.imagen_usuario = self.cargar_imagen(ruta_imagen_usuario, (150, 150))

        #-------------------------------------------------------------------------------#
        # Creación de la interfaz gráfica
        #-------------------------------------------------------------------------------#

        frame = tk.Frame(self, bg="#333333")
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        #-------------------------------------------------------------------------------#
        # Imagen de usuario 
        #-------------------------------------------------------------------------------#

        if self.imagen_usuario:
            etiqueta_imagen = tk.Label(frame, image=self.imagen_usuario, bg="#333333")
            etiqueta_imagen.grid(row=2, column=0, rowspan=3, padx=10, pady=10)

        #-------------------------------------------------------------------------------#
        # Sección de login en la parte derecha
        #-------------------------------------------------------------------------------#

        tk.Label(frame, text="LOGIN", font=("Comic Sans MS", 18, "bold"), fg="#FFBF00", bg="#333333").grid(row=1, column=1, pady=3)

        tk.Label(frame, text="Usuario:", font=("Comic Sans MS", 12), fg="#EF8114", bg="#333333").grid(row=2, column=1, sticky="w")
        self.entrada_usuario = tk.Entry(frame, width=20, font=("Comic Sans MS", 12))
        self.entrada_usuario.grid(row=2, column=2, pady=5)

        tk.Label(frame, text="Contraseña:", font=("Comic Sans MS", 12), fg="#EF8114", bg="#333333").grid(row=3, column=1, sticky="w")
        self.entrada_contraseña = tk.Entry(frame, show="*", width=20, font=("Comic Sans MS", 12))
        self.entrada_contraseña.grid(row=3, column=2, pady=5)

        #-------------------------------------------------------------------------------#
        # Botones de la aplicación con efectos de hover y clic
        #-------------------------------------------------------------------------------#

        boton_login = tk.Button(frame, text="Iniciar sesión", command=self.iniciar_sesion, 
                      font=("Comic Sans MS", 12, "bold"), bg="#FF7F50", fg="white", relief="flat",
                      width=20, bd=2, highlightbackground="#333333", highlightcolor="#333333")
        boton_login.grid(row=4, column=1, columnspan=2, pady=5)
        boton_login.bind("<Enter>", lambda event: boton_login.config(bg="#32CD32"))  # Cambia el color al pasar el mouse
        boton_login.bind("<Leave>", lambda event: boton_login.config(bg="#FF7F50"))  # Vuelve al color original
        boton_login.bind("<Button-1>", lambda event: boton_login.config(bg="#FF4500"))  # Efecto al hacer clic

        boton_salir = tk.Button(frame, text="Salir", command=self.quit, 
                     font=("Comic Sans MS", 12, "bold"), bg="#FF7F50", fg="white", relief="flat",
                     width=20, bd=2, highlightbackground="#333333", highlightcolor="#333333")
        boton_salir.grid(row=5, column=1, columnspan=2, pady=5)
        boton_salir.bind("<Enter>", lambda event: boton_salir.config(bg="#FF0000"))
        boton_salir.bind("<Leave>", lambda event: boton_salir.config(bg="#FF7F50"))
        boton_salir.bind("<Button-1>", lambda event: boton_salir.config(bg="#FF4500"))

    #-------------------------------------------------------------------------------#
    # Función para cargar y redimensionar imágenes
    #-------------------------------------------------------------------------------#

    def cargar_imagen(self, ruta, tamaño):
        try:
            imagen = Image.open(ruta)
            imagen = imagen.convert("RGB")  
            imagen = imagen.resize(tamaño, Image.Resampling.LANCZOS)  
            return ImageTk.PhotoImage(imagen)
        except Exception as e:
            print(f"Error cargando {ruta}: {e}")
            return None

    #-------------------------------------------------------------------------------#
    # Función para manejar el login 
    #-------------------------------------------------------------------------------#

    def iniciar_sesion(self):
        usuario = self.entrada_usuario.get()
        contraseña = self.entrada_contraseña.get()

        # Comprobar si los campos están vacíos
        if not usuario or not contraseña:
            messagebox.showerror("Error", "Introduce los datos. No puede estar vacío.")
            return

        # Datos predefinidos (supuesto usuario y contraseña)
        usuario_valido = "usuario"
        contraseña_valida = "contraseña"

        # Comprobar si los datos son correctos
        if usuario == usuario_valido and contraseña == contraseña_valida:
            messagebox.showinfo("Bienvenido", "¡Bienvenido!")
            self.after(1000, self.cargar_home)  # Espera 1 segundo antes de abrir home.py
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    #-------------------------------------------------------------------------------#
    # Cargar el archivo home.py cuando los datos son correctos
    #-------------------------------------------------------------------------------#
    def cargar_home(self):
        self.quit()  # Cierra la ventana de login
        
        # Cambia la ruta según donde esté ubicado home.py
        ruta_home = os.path.join(os.path.dirname(__file__), "home.py")
        
        # Verificar si el archivo existe en la ruta
        if os.path.exists(ruta_home):
            subprocess.Popen(["python", ruta_home], shell=True)
        else:
            messagebox.showerror("Error", "No se pudo encontrar el archivo home.py.")
        
#-------------------------------------------------------------------------------#
# Punto de entrada de la aplicación
#-------------------------------------------------------------------------------#

if __name__ == "__main__":
    app = AplicacionLogin()
    app.mainloop()