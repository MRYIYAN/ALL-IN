#-------------------------------------------------------------------------------#
# Imports necesarios para la funcionalidad del programa
#-------------------------------------------------------------------------------#

import tkinter as tk  # Importa la librería de Tkinter pip install Tkinter
from PIL import Image, ImageTk  # Importa la librería PIL pip install pillow
from tkinter import messagebox  # Importa la librería para ventanas emergentes

#-------------------------------------------------------------------------------#
# Clase principal de la aplicación de Login
#-------------------------------------------------------------------------------#

class LoginApp(tk.Tk):
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
        self.iconbitmap("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.ico")  

        #-------------------------------------------------------------------------------#
        # Carga de la imagen de usuario 
        #-------------------------------------------------------------------------------#

        self.user_image = self.load_image("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/user.png", (150, 150))

        #-------------------------------------------------------------------------------#
        # Creación de la interfaz gráfica
        #-------------------------------------------------------------------------------#

        frame = tk.Frame(self, bg="#333333")
        frame.pack(expand=True, fill="both", padx=20, pady=20)

        #-------------------------------------------------------------------------------#
        # Imagen de usuario 
        #-------------------------------------------------------------------------------#

        if self.user_image:
            image_label = tk.Label(frame, image=self.user_image, bg="#333333")
            image_label.grid(row=2, column=0, rowspan=3, padx=10, pady=10)

        #-------------------------------------------------------------------------------#
        # Sección de login en la parte derecha
        #-------------------------------------------------------------------------------#

        tk.Label(frame, text="LOGIN", font=("Comic Sans MS", 18, "bold"), fg="#FFBF00", bg="#333333").grid(row=1, column=1, pady=3)

        tk.Label(frame, text="Usuario:", font=("Comic Sans MS", 12), fg="#EF8114", bg="#333333").grid(row=2, column=1, sticky="w")
        self.entry_user = tk.Entry(frame, width=20, font=("Comic Sans MS", 12))
        self.entry_user.grid(row=2, column=2, pady=5)

        tk.Label(frame, text="Contraseña:", font=("Comic Sans MS", 12), fg="#EF8114", bg="#333333").grid(row=3, column=1, sticky="w")
        self.entry_pass = tk.Entry(frame, show="*", width=20, font=("Comic Sans MS", 12))
        self.entry_pass.grid(row=3, column=2, pady=5)

        #-------------------------------------------------------------------------------#
        # Botones de la aplicación con efectos de hover y clic
        #-------------------------------------------------------------------------------#

        btn_login = tk.Button(frame, text="Iniciar sesión", command=self.login, 
                      font=("Comic Sans MS", 12, "bold"), bg="#FF7F50", fg="white", relief="flat",
                      width=20, bd=2, highlightbackground="#333333", highlightcolor="#333333")
        btn_login.grid(row=4, column=1, columnspan=2, pady=5)
        btn_login.bind("<Enter>", lambda event: btn_login.config(bg="#32CD32"))  # Cambia el color al pasar el mouse
        btn_login.bind("<Leave>", lambda event: btn_login.config(bg="#FF7F50"))  # Vuelve al color original
        btn_login.bind("<Button-1>", lambda event: btn_login.config(bg="#FF4500"))  # Efecto al hacer clic

        btn_exit = tk.Button(frame, text="Salir", command=self.quit, 
                     font=("Comic Sans MS", 12, "bold"), bg="#FF7F50", fg="white", relief="flat",
                     width=20, bd=2, highlightbackground="#333333", highlightcolor="#333333")
        btn_exit.grid(row=5, column=1, columnspan=2, pady=5)
        btn_exit.bind("<Enter>", lambda event: btn_exit.config(bg="#FF0000"))
        btn_exit.bind("<Leave>", lambda event: btn_exit.config(bg="#FF7F50"))
        btn_exit.bind("<Button-1>", lambda event: btn_exit.config(bg="#FF4500"))

    #-------------------------------------------------------------------------------#
    # Función para cargar y redimensionar imágenes
    #-------------------------------------------------------------------------------#

    def load_image(self, path, size):
        try:
            image = Image.open(path)
            image = image.convert("RGB")  
            image = image.resize(size, Image.Resampling.LANCZOS)  
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error cargando {path}: {e}")
            return None

    #-------------------------------------------------------------------------------#
    # Función para manejar el login 
    #-------------------------------------------------------------------------------#

    def login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()

        # Comprobar si los campos están vacíos
        if not username or not password:
            messagebox.showerror("Error", "Introduce los datos. No puede estar vacío.")
            return

        # Datos predefinidos (supuesto usuario y contraseña)
        valid_username = "usuario"
        valid_password = "contraseña"

        # Comprobar si los datos son correctos
        if username == valid_username and password == valid_password:
            messagebox.showinfo("Bienvenido", "¡Bienvenido!")
            self.after(1000, self.load_home)  # Espera 1 segundo antes de abrir home.py
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")

    #-------------------------------------------------------------------------------#
    # Cargar el archivo home.py cuando los datos son correctos
    #-------------------------------------------------------------------------------#
    def load_home(self):
        self.destroy()  # Cierra la ventana de login
        
        # Cambia la ruta según donde esté ubicado home.py
        import os
        home_path = "C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/home.py"
        
        # Verificar si el archivo existe en la ruta
        if os.path.exists(home_path):
            exec(open(home_path).read())  # Ejecuta home.py
        else:
            messagebox.showerror("Error", "No se pudo encontrar el archivo home.py.")
        
#-------------------------------------------------------------------------------#
# Punto de entrada de la aplicación
#-------------------------------------------------------------------------------#

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
