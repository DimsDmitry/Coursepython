import json

import requests
import telebot

from key import SECRET_KEY


bot = telebot.TeleBot(SECRET_KEY)
API = '135b46a59fd34bb8f2b485d430aa50d7'

# если поступила команда /start, запусти функцию start
@bot.message_handler(commands=['start'])
def start(message):
    """получает от пользователя объект message"""
    # отправляем пользователю приветствие, просим ввести город
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


# обработаем ввод города
@bot.message_handler(content_types=['text'])
# если пришёл тип данных "текст" (не команда, не фото), ТО запускаем функцию get_weather
def get_weather(message):
    """конвертирует текст пользователя в название города, делает запрос к сайту с этим городом,
    получает ответ в формате json-файл"""
    # получим из сообщения название города, очистим его от лишних пробелов, все буквы в нижний регистр
    city = message.text.strip().lower()
    # сформируем шаблон запроса, учитывая город и наш API-ключ
    api_call = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}'
    # отправляем запрос на погодный сервис
    result = requests.get(api_call)
    # далее модуль json превращает сложный текстовый ответ в понятный для Python формат - словарь
    # словарь помещается в переменную дата
    data = json.loads(result.text)
    # полученное значение - словарь. извлекаем из него по ключам main и temp температуру,
    # переводим из градусов Кельвина в градусы Цельсия, округляем до сотых
    temperature = round(data['main']['temp'] - 273.15, 2)
    # отправляем пользователю сообщение с ответом
    bot.reply_to(message, f'Сейчас температура: {temperature} °C')

# Команда, которая запускает бота. Он начинает постоянно опрашивать сервер телеграмм,
# на каждой итерации проверяет нет ли новых сообщений
bot.polling(none_stop=True)
# none_stop=True - бот продолжит работать даже если возникла ошибка