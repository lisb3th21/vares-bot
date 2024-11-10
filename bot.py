# bot.py

import os
from dotenv import load_dotenv
import tweepy
from datetime import datetime

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def read_actual_day():
    try:
        with open("contador_dias.txt", "r") as file:
            day = int(file.read())
    except FileNotFoundError:
        day = 1  
    return day

def update_day():
    day = read_actual_day() + 1
    with open("contador_dias.txt", "w") as file:
        file.write(str(day))
    return day

def post():
    dia_actual = read_actual_day()
    mensaje = f"Día {dia_actual} esperando a que Vares regrese."
    api.update_status(mensaje)
    print(f"Tuiteado: {mensaje}")
    update_day()

if __name__ == "__main__":
    post()
