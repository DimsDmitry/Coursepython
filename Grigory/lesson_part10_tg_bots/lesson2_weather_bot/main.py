import json

import requests
import telebot

from key import SECRET_KEY


bot = telebot.TeleBot(SECRET_KEY)
API = '135b46a59fd34bb8f2b485d430aa50d7 '

# если поступила команда /start, запусти функцию start
@bot.message_handler(commands=['start'])
def start(message):
    """получает от пользователя объект message"""
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')