import telebot
from telebot import types

from key import KEY

# инициализируем бота, передаём в него токен (ключ доступа)
bot = telebot.TeleBot(KEY)

# глобальная переменная для хранения счёта
# она будет жить вне функций, чтобы быть доступной во всех частях программы
score = 0

# Шаг 1 - запуск квиза
@bot.message_handler(commands=['start'])
def start_quiz(message):
    """Функция срабатывает при команде /start"""
    global score  # указываем переменную глобальной
    score = 0

    # создаём кнопки, которые будут выводиться вместе с сообщением:
    markup = types.InlineKeyboardMarkup()

    # создаём кнопки, которые будут входить в markup,
    # callback_data - скрытый текст, который бот получит при нажатии кнопки
    btn1 = types.InlineKeyboardButton(text='Python', callback_data='q1_correct')
    btn2 = types.InlineKeyboardButton(text='Java', callback_data='q1_wrong')

    # добавляем кнопки в объект markup
    markup.add(btn1, btn2)

    # Отправляем первое сообщение пользователю, прикрепляем клавиатуру:
    bot.send_message(message.chat.id,
                     'Начинаем наш квиз!\nВопрос №1: Какой язык мы сейчас изучаем?',
                    reply_markup=markup)

# Шаг 2 - логика игры (обработка всех нажатий)
@bot.callback_query_handler(func=lambda call: True)
# "слушатель" кнопок - если кнопка нажата возвращает True (принимает нажатие любой кнопки)
def handle_quiz(call):
    global score  # указываем переменную глобальной

    # проверяем содержимое callback_data нажатой кнопки
    # если есть приписка _correct, то ответ верный
    if '_correct' in call.data:
        score += 1  # увеличиваем счёт
        # выводим ответ:
        bot.answer_callback_query(call.id, 'Верно!')

    # если в данных есть "_wrong", ответ неверный
    elif '_wrong' in call.data:
        # выводим ответ:
        bot.answer_callback_query(call.id, 'Ошибка!')

    # Логика переходов: проверяем с помощью первых двух символов callback_data, где мы сейчас находимся
    # q1 - первый вопрос, q2 - второй и тд
    if 'q1' in call.data:
        send_question(call.message, 2)
    elif 'q2' in call.data:
        send_question(call.message, 3)
    elif 'q3' in call.data:
        send_question(call.message, 4)
    elif 'q4' in call.data:
        send_question(call.message, 5)
    elif 'q5' in call.data:
        # если ответили на крайний вопрос - показываем итог
        show_result(call.message)


# Шаг 3 - конструктор вопросов
def send_question(message, num):
    """Функция получает номер вопроса num и обновляет сообщение.
    Использует edit_message_text"""

    markup = types.InlineKeyboardMarkup()
    if num == 2:
        text = "Вопрос №2. Можно ли сочетать операторы 'and' и 'or' в одном условии?"
        btn1 = types.InlineKeyboardButton(text='Да', callback_data='q2_correct')
        btn2 = types.InlineKeyboardButton(text='Нет', callback_data='q2_wrong')
        markup.add(btn1, btn2)  # перезаписываем кнопки, добавляем в уже созданный markup

    elif num == 3:
        text = "Вопрос №3. Что делает оператор 'and'?"
        btn1 = types.InlineKeyboardButton(text='Проверяет, что ХОТЯ БЫ ОДНО условие верно', callback_data='q3_wrong')
        btn2 = types.InlineKeyboardButton(text='Проверяет, что ОБА условия верны', callback_data='q3_correct')
        markup.add(btn1, btn2)  # перезаписываем кнопки, добавляем в уже созданный markup

    elif num == 4:
        text = "Вопрос №4. Какой символ ставится в конце строки с условным оператором if/elif/else?"
        btn1 = types.InlineKeyboardButton(text='Точка (.)', callback_data='q4_wrong')
        btn2 = types.InlineKeyboardButton(text='Двоеточие (:)', callback_data='q4_correct')
        markup.add(btn1, btn2)  # перезаписываем кнопки, добавляем в уже созданный markup

    elif num == 5:
        text = "Вопрос 5. Какой тип данных изменяемым из указанных?"
        btn1 = types.InlineKeyboardButton(text='Кортеж', callback_data='q5_wrong')
        btn2 = types.InlineKeyboardButton(text='Список', callback_data='q5_correct')
        markup.add(btn1, btn2)  # перезаписываем кнопки, добавляем в уже созданный markup

    # edit_message_text изменяет текущее сообщение, чтобы не засорять чат новыми сообщениями
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=text, reply_markup=markup)

# Шаг 4
def show_result(message):
    """Рассчитывает результат игрока на основе набранных баллов"""
    if score == 5:
        result = 'Программист-легенда!'
    elif 3 <= score < 5:
        result = 'Крепкий Миддл!'
    elif 1 <= score < 3:
        result = 'Начинающий Юниор...'
    else:
        result = 'Нужно больше практики...'

    text = f"Квиз завершён!\n\nТвой результат: {score} из 5.\nЗвание: {result}\nНажми /start чтобы начать заново!"
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=text)

# Запуск бота!
bot.polling(none_stop=True)