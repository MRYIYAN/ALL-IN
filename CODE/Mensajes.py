# -------------------------------------------------------------------------------#
# Imports necesarios para la funcionalidad de la ventana
# -------------------------------------------------------------------------------#
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

        #-------------------------------------------------------------------------------
        # Configuración de la ventana
        #-------------------------------------------------------------------------------
        self.title("ALL-IN V1.0 - Mensajes")
        self.geometry("640x600")  
        self.configure(bg="#f0f0f0")
        self.iconbitmap(os.path.join(os.path.dirname(__file__), "assets/allin.ico"))  # Icono de la ventana

        #-------------------------------------------------------------------------------
        # Barra de navegación
        #-------------------------------------------------------------------------------
        self.navbar = tk.Frame(self, bg="#333333")
        self.navbar.pack(fill="x", side="top", padx=0, pady=0)
        self.crear_navbar()

        #-------------------------------------------------------------------------------
        # Encabezado
        #-------------------------------------------------------------------------------
        encabezado = tk.Label(self, text="TUS MENSAJES", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        encabezado.pack(pady=(10, 5))

        #-------------------------------------------------------------------------------
        # Área de mensajes
        #-------------------------------------------------------------------------------
        self.area_mensajes = tk.Frame(self, bg="#f0f0f0")  # Eliminé el 'bd' para quitar el borde
        self.area_mensajes.pack(pady=10, padx=10, fill="both", expand=True)

        #-------------------------------------------------------------------------------
        # Área de chat
        #-------------------------------------------------------------------------------
        self.chat_area = tk.Text(self.area_mensajes, font=("Helvetica", 12), bg="#fff", fg="#333333", wrap="word", height=10, width=60)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.insert(tk.END, "Bot -> Bienvenido a tu centro de mensajes. Escribe aquí...\n")
        self.chat_area.config(state=tk.DISABLED)

        #-------------------------------------------------------------------------------
        # Entrada de usuario
        #-------------------------------------------------------------------------------
        self.e = tk.Entry(self, bg="#fff", fg="#333333", font=("Helvetica", 12), width=50)
        self.e.pack(pady=(5, 0), padx=10)  # Se mantiene cerca del chat

        #-------------------------------------------------------------------------------
        # Botón para enviar mensaje
        #-------------------------------------------------------------------------------
        self.boton_enviar_chat = tk.Button(self, text="Enviar", font=("Helvetica", 12, "bold"), bg="#ABB2B9", command=self.enviar_mensaje_chat)
        self.boton_enviar_chat.pack(pady=(0, 15))  # Mantiene el espacio mínimo entre la entrada y el botón

        #-------------------------------------------------------------------------------
        # Pie de página
        #-------------------------------------------------------------------------------
        self.footer = tk.Frame(self, bg="#FFA500", height=50)
        self.footer.pack(fill="x", side="bottom", pady=0)

        #-------------------------------------------------------------------------------
        # Iconos de redes sociales
        #-------------------------------------------------------------------------------
        self.iconos_redes = tk.Frame(self.footer, bg="#FFA500")
        self.iconos_redes.pack(side="left", padx=10, pady=5)
        self.cargar_iconos_redes()

        #-------------------------------------------------------------------------------
        # Enlace web
        #-------------------------------------------------------------------------------
        enlace_web = tk.Label(self.footer, text="Visita nuestra web", fg="white", bg="#FFA500", cursor="hand2", font=("Arial", 10, "underline"))
        enlace_web.pack(side="right", padx=10, pady=5)
        enlace_web.bind("<Button-1>", lambda e: self.abrir_pagina("https://dev-h3ctor23.github.io/"))

    def crear_navbar(self):
        #-------------------------------------------------------------------------------
        # Crear la barra de navegación
        #-------------------------------------------------------------------------------
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

    def crear_boton(self, texto, columna):
        #-------------------------------------------------------------------------------
        # Crear botones en la barra de navegación
        #-------------------------------------------------------------------------------
        boton = tk.Button(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat", command=lambda: self.al_hacer_clic(texto))
        boton.grid(row=0, column=columna, padx=20, pady=10)

    def crear_boton_desplegable(self, texto, columna, opciones):
        #-------------------------------------------------------------------------------
        # Crear botones desplegables en la barra de navegación
        #-------------------------------------------------------------------------------
        desplegable = tk.Menubutton(self.navbar, text=texto, font=("Arial", 12), fg="white", bg="#333333", relief="flat")
        menu = tk.Menu(desplegable, tearoff=0, bg="#333333", fg="white")
        for opcion in opciones:
            menu.add_command(label=opcion, command=lambda opt=opcion: self.al_hacer_clic(opt))
        desplegable.config(menu=menu)
        desplegable.grid(row=0, column=columna, padx=20, pady=10)

    def al_hacer_clic(self, texto_boton):
        #-------------------------------------------------------------------------------
        # Acciones al hacer clic en un botón de la barra de navegación
        #-------------------------------------------------------------------------------
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
            messagebox.showinfo(texto_boton, f"Has hecho clic en '{texto_boton}'.")

    def cerrar_y_abrir(self, ruta):
        #-------------------------------------------------------------------------------
        # Cerrar la aplicación actual y abrir otra
        #-------------------------------------------------------------------------------
        self.quit()
        subprocess.Popen(["python", ruta], shell=True)

    def enviar_mensaje_chat(self):
        #-------------------------------------------------------------------------------
        # Enviar mensaje desde el chat
        #-------------------------------------------------------------------------------
        mensaje = self.e.get().lower()

        # Eliminar acentos y signos de puntuación
        mensaje = unidecode.unidecode(mensaje)  # Eliminar acentos
        mensaje = mensaje.strip("!¿?.,;:")  # Eliminar signos de puntuación no deseados

        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"Tú -> {mensaje}\n")
        self.chat_area.yview(tk.END)

        # Respuestas ampliadas para hacerlo más funcional
        respuestas = {
        # Variaciones de saludos
        "hola": "Bot -> ¡Hola! ¿Cómo puedo ayudarte?",
        "buenos dias": "Bot -> ¡Buenos días! ¿Cómo estás?",
        "buenas tardes": "Bot -> ¡Buenas tardes! ¿Qué tal tu día?",
        "buenas noches": "Bot -> ¡Buenas noches! ¿Todo bien?",
        "que tal": "Bot -> ¡Todo bien! ¿Y tú?",
        "hey": "Bot -> ¡Hey! ¿Cómo te puedo ayudar?",
        "que onda": "Bot -> ¡Qué onda! ¿En qué te puedo ayudar?",
        "hi": "Bot -> Hi! How can I assist you today?",
        "saludos": "Bot -> ¡Saludos! ¿Cómo va todo?",
        
        # Variaciones de "cómo estás"
        "como estas": "Bot -> Estoy bien, ¿y tú?",
        "como te va": "Bot -> Me va genial, gracias por preguntar. ¿Y a ti?",
        "que tal todo": "Bot -> Todo bien, ¿y tú? ¿Cómo va todo?",
        "como te encuentras": "Bot -> Todo tranquilo por aquí, ¿y tú?",
        
        # Respuesta estándar
        "gracias": "Bot -> ¡De nada! ¿En qué más te puedo ayudar?",
        "adios": "Bot -> ¡Hasta luego! ¡Cuídate!",
        "bye": "Bot -> Goodbye! Have a great day!",
        "nos vemos": "Bot -> ¡Nos vemos pronto!",
        
        # Respuestas para obtener más información
        "quien eres": "Bot -> Soy un asistente virtual creado para ayudarte. ¿En qué te puedo asistir?",
        "que haces": "Bot -> Estoy aquí para responder tus preguntas y ayudarte en lo que necesites.",
        "tu nombre": "Bot -> Mi nombre es Bot. ¿Y el tuyo?",
        "como te llamas": "Bot -> Me llamo Bot, ¿cómo te llamas tú?",
        
        # Consultas de hora
        "que hora es": "Bot -> La hora actual es: " + self.obtener_hora_actual(),
        "hora actual": "Bot -> Son las " + self.obtener_hora_actual(),
        "me dices la hora": "Bot -> Claro, la hora es: " + self.obtener_hora_actual(),
        "que hora tienes": "Bot -> Tengo la hora: " + self.obtener_hora_actual(),
        "hora": "Bot -> La hora en este momento es: " + self.obtener_hora_actual(),
        
        # Preguntas frecuentes
        "ayuda": "Bot -> ¿En qué puedo ayudarte? Puedo responder preguntas o darte información.",
        "que puedes hacer": "Bot -> Puedo responder preguntas, ofrecerte ayuda y guiarte en tus actividades.",
        "como puedo contactarte": "Bot -> Siempre estaré disponible aquí para ti. ¡Solo escribe tu mensaje!",
        "tienes redes sociales": "Bot -> No tengo, pero te puedo dirigir a nuestras redes sociales. ¿Te interesa?",
        "donde te encuentro": "Bot -> Estoy aquí, en este chat. ¿En qué puedo ayudarte hoy?",
        
        # Respuestas humorísticas o curiosas
        "cuantos años tienes": "Bot -> No tengo edad, soy solo un asistente virtual. ¿Tú cuántos años tienes?",
        "quien es el mejor": "Bot -> ¡Tú eres el mejor! Siempre aquí para ayudarte.",
        "cual es tu comida favorita": "Bot -> No como, pero me gusta pensar que los bits son mi comida favorita.",
        "que opinas de los humanos": "Bot -> ¡Los humanos son geniales! Son los que me hacen funcionar.",
        
        # Respuestas diversas
        "como puedo ayudarte": "Bot -> Puedes preguntarme cualquier cosa, ¡aquí estoy para lo que necesites!",
        "estoy aburrido": "Bot -> ¡Vaya! ¿Por qué no pruebas hacer algo divertido? ¡Puedo recomendarte actividades!",
        "quiero saber mas": "Bot -> Claro, ¿sobre qué te gustaría saber más?",
        
        # Respuestas para no entender algo
        "": "Bot -> ¡Hola! Parece que no escribiste nada. ¿Cómo puedo ayudarte?",
        "lo siento": "Bot -> No te preocupes, ¿qué más necesitas?",
        "no entiendo": "Bot -> ¡No hay problema! Puedes preguntar lo que necesites.",
        "no se": "Bot -> Si no sabes algo, ¡yo estoy aquí para ayudarte a encontrarlo!"
}
        
        respuesta = respuestas.get(mensaje, "Bot -> Lo siento, no entendí esa pregunta.")
        self.chat_area.insert(tk.END, f"{respuesta}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.e.delete(0, tk.END)

    def obtener_hora_actual(self):
        #-------------------------------------------------------------------------------
        # Obtener la hora actual
        #-------------------------------------------------------------------------------
        from datetime import datetime
        return datetime.now().strftime("%H:%M")

    def cargar_iconos_redes(self):
        #-------------------------------------------------------------------------------
        # Cargar iconos de redes sociales en el pie de página
        #-------------------------------------------------------------------------------
        iconos = ["facebook.png", "twitter.png", "instagram.png"]
        for icono in iconos:
            img = self.cargar_imagen(os.path.join(os.path.dirname(__file__), f"assets/{icono}"), (25, 25))
            if img:
                etiqueta = tk.Label(self.iconos_redes, image=img, bg="#FFA500")
                etiqueta.image = img
                etiqueta.pack(side="left", padx=5)

    def abrir_pagina(self, url):
        #-------------------------------------------------------------------------------
        # Abrir una URL en el navegador
        #-------------------------------------------------------------------------------
        webbrowser.open(url)

    def cargar_imagen(self, ruta, tamaño):
        #-------------------------------------------------------------------------------
        # Cargar una imagen desde una ruta
        #-------------------------------------------------------------------------------
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
