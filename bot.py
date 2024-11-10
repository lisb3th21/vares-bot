# bot.py

import os
from dotenv import load_dotenv
import tweepy
from datetime import datetime

# Cargar credenciales desde el archivo .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Autenticación de Twitter usando las credenciales cargadas
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Leer el conteo actual de días desde un archivo
def leer_dia_actual():
    try:
        with open("contador_dias.txt", "r") as file:
            dia = int(file.read())
    except FileNotFoundError:
        dia = 1  # Inicia en 1 si el archivo no existe
    return dia

# Incrementar y guardar el nuevo conteo de días
def actualizar_dia():
    dia = leer_dia_actual() + 1
    with open("contador_dias.txt", "w") as file:
        file.write(str(dia))
    return dia

# Tuitear el mensaje diario
def tuitear_contador():
    dia_actual = leer_dia_actual()
    mensaje = f"Día {dia_actual} esperando a que Vares regrese."
    api.update_status(mensaje)
    print(f"Tuiteado: {mensaje}")
    actualizar_dia()

# Ejecuta la función principal para tuitear
if __name__ == "__main__":
    tuitear_contador()
