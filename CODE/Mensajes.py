import tkinter as tk
import subprocess  # Para abrir otros archivos Python
from tkinter import messagebox
from PIL import Image, ImageTk  # Para cargar y mostrar imágenes
import webbrowser  # Para abrir URLs en el navegador
import os  # Para trabajar con el sistema de archivos
import unidecode  # Para eliminar acentos pip install unicode

class MensajesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ALL-IN V1.0 - Mensajes")
        self.geometry("640x600")  
        self.configure(bg="#f0f0f0")
        self.iconbitmap("C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/allin.ico")  
        
        # Barra de navegación
        self.navbar = tk.Frame(self, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        self.crear_navbar()

        # Encabezado
        encabezado = tk.Label(self, text="TUS MENSAJES", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))

        # Área de mensajes (sin el borde)
        self.area_mensajes = tk.Frame(self, bg="#f0f0f0")  # Eliminé el 'bd' para quitar el borde
        self.area_mensajes.pack(pady=10, padx=10, fill="both", expand=True)

        # Chatbot área
        self.chat_area = tk.Text(self.area_mensajes, font=("Helvetica", 12), bg="#fff", fg="#333333", wrap="word", height=10, width=60)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.insert(tk.END, "Bot -> Bienvenido a tu centro de mensajes. Escribe aquí...\n")
        self.chat_area.config(state=tk.DISABLED)

        # Entrada de usuario (ajustada para estar más cerca del chat)
        self.e = tk.Entry(self, bg="#fff", fg="#333333", font=("Helvetica", 12), width=50)
        self.e.pack(pady=(5, 0), padx=10)  # Se mantiene cerca del chat

        # Botón para enviar mensaje (ajustado para estar más cerca de la entrada)
        self.boton_enviar_chat = tk.Button(self, text="Enviar", font=("Helvetica", 12, "bold"), bg="#ABB2B9", command=self.enviar_mensaje_chat)
        self.boton_enviar_chat.pack(pady=(0, 15))  # Mantiene el espacio mínimo entre la entrada y el botón

        # Pie de página
        self.footer = tk.Frame(self, bg="#FFA500", height=50)
        self.footer.pack(fill="x", side="bottom", pady=0)

        # Redes sociales
        self.iconos_redes = tk.Frame(self.footer, bg="#FFA500")
        self.iconos_redes.pack(side="left", padx=10, pady=5)
        self.cargar_iconos_redes()

        # Enlace (derecha)
        enlace_web = tk.Label(self.footer, text="Visita nuestra web", fg="white", bg="#FFA500", cursor="hand2", font=("Arial", 10, "underline"))
        enlace_web.pack(side="right", padx=10, pady=5)
        enlace_web.bind("<Button-1>", lambda e: self.abrir_pagina("https://tupagina.com"))

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

    def crear_boton(self, texto, columna):
        boton = tk.Button(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat", command=lambda: self.al_hacer_clic(texto))
        boton.grid(row=0, column=columna, padx=20, pady=10)

    def crear_boton_desplegable(self, texto, columna, opciones):
        desplegable = tk.Menubutton(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat")
        menu = tk.Menu(desplegable, tearoff=0, bg="#333333", fg="white")
        for opcion in opciones:
            menu.add_command(label=opcion, command=lambda opt=opcion: self.al_hacer_clic(opt))
        desplegable.config(menu=menu)
        desplegable.grid(row=0, column=columna, padx=20, pady=10)

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
            messagebox.showinfo(texto_boton, f"Has hecho clic en '{texto_boton}'.")

    def cerrar_y_abrir(self, ruta):
        self.quit()
        subprocess.Popen(["python", ruta], shell=True)

    def enviar_mensaje_chat(self):
        mensaje = self.e.get().lower()

        # Eliminar acentos y signos de puntuación
        mensaje = unidecode.unidecode(mensaje)  # Eliminar acentos
        mensaje = mensaje.strip("!¿?.,;:")  # Eliminar signos de puntuación no deseados

        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"Tú -> {mensaje}\n")
        self.chat_area.yview(tk.END)

        respuestas = {
            "hola": "Bot -> ¡Hola! ¿Cómo puedo ayudarte?",
            "como estas": "Bot -> Estoy bien, ¿y tú?",
            "gracias": "Bot -> ¡De nada!",
            "adios": "Bot -> ¡Hasta luego!",
            "quien eres": "Bot -> Soy un asistente virtual creado para ayudarte.",
            "que hora es": "Bot -> La hora actual es: " + self.obtener_hora_actual(),
            "tu nombre": "Bot -> Mi nombre es Bot, ¿y el tuyo?",
            "ayuda": "Bot -> ¿En qué puedo ayudarte? Puedo responder preguntas o darte información.",
            "que haces": "Bot -> Estoy aquí para ayudarte con cualquier pregunta que tengas.",
            "como puedo contactarte": "Bot -> Siempre estaré disponible aquí para ti.",
            "tienes redes sociales": "Bot -> No tengo, pero te puedo dirigir a nuestras redes sociales."
        }

        respuesta = respuestas.get(mensaje, "Bot -> Lo siento, no entendí esa pregunta.")
        self.chat_area.insert(tk.END, f"{respuesta}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.e.delete(0, tk.END)

    def obtener_hora_actual(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M")

    def cargar_iconos_redes(self):
        iconos = ["facebook.png", "twitter.png", "instagram.png"]
        for icono in iconos:
            img = self.cargar_imagen(f"C:/Users/ian00/Documents/GitHub/ALL-IN/CODE/assets/{icono}", (25, 25))
            if img:
                etiqueta = tk.Label(self.iconos_redes, image=img, bg="#FFA500")
                etiqueta.image = img
                etiqueta.pack(side="left", padx=5)

    def abrir_pagina(self, url):
        webbrowser.open(url)

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
    app = MensajesApp()
    app.mainloop()
