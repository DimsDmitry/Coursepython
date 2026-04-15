import telebot
from telebot import types
import logging

# --- НАСТРОЙКА ЛОГИРОВАНИЯ ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='quiz_oop.log',
    filemode='a',
    encoding='utf-8'
)

bot = telebot.TeleBot('ВАШ_ТОКЕН')


# --- КЛАСС "ВОПРОС" (ООП) ---
class Question:
    def __init__(self, text, options):
        self.text = text  # Текст вопроса
        self.options = options  # Список кортежей: [("Текст", "status"), ...]

    def create_keyboard(self, index):
        """Метод объекта для создания собственной клавиатуры"""
        markup = types.InlineKeyboardMarkup()
        for opt_text, status in self.options:
            # Формируем callback_data, передавая индекс вопроса и статус ответа
            callback_data = f"{index}_{status}"
            markup.add(types.InlineKeyboardButton(opt_text, callback_data=callback_data))
        return markup


# --- СОЗДАНИЕ СПИСКА ОБЪЕКТОВ ---
# Теперь каждый элемент списка — это экземпляр класса Question
QUIZ_DATA = [
    Question("Какой язык мы сейчас изучаем?", [("Python", "correct"), ("Java", "wrong")]),
    Question("Используем ли мы ООП в этом коде?", [("Да", "correct"), ("Нет", "wrong")]),
    Question("Что такое класс?", [("Чертеж объекта", "correct"), ("Просто функция", "wrong")]),
    Question("Как называется метод-конструктор в Python?", [("__init__", "correct"), ("start()", "wrong")]),
    Question("Для чего нужно логирование?", [("Для отслеживания работы", "correct"), ("Для красоты", "wrong")])
]

# Глобальный счет (для простоты урока)
score = 0


# --- ОБРАБОТЧИК /START ---
@bot.message_handler(commands=['start'])
def start_quiz(message):
    global score
    score = 0
    logging.info(f"Юзер {message.from_user.id} начал квиз на базе ООП.")

    # Берем самый первый объект вопроса из списка
    first_q = QUIZ_DATA[0]
    bot.send_message(
        message.chat.id,
        f"❓ Вопрос №1: {first_q.text}",
        reply_markup=first_q.create_keyboard(0)
    )


# --- ОБРАБОТКА НАЖАТИЙ ---
@bot.callback_query_handler(func=lambda call: True)
def handle_answer(call):
    global score

    # Разбираем данные из нажатой кнопки
    data_parts = call.data.split("_")
    current_index = int(data_parts[0])
    status = data_parts[1]

    # Проверка правильности
    if status == "correct":
        score += 1
        bot.answer_callback_query(call.id, "Правильно! ✅")
    else:
        bot.answer_callback_query(call.id, "Неверно! ❌")

    # Переход к следующему объекту вопроса
    next_index = current_index + 1

    if next_index < len(QUIZ_DATA):
        next_q = QUIZ_DATA[next_index]  # Берем следующий объект из списка
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"❓ Вопрос №{next_index + 1}: {next_q.text}",
            reply_markup=next_q.create_keyboard(next_index)  # Объект сам создает себе кнопки
        )
    else:
        show_result(call.message)


# --- ФИНАЛ ---
def show_result(message):
    total = len(QUIZ_DATA)
    rank = "Профи ООП! 💎" if score == total else "Хороший результат! 👍"

    final_text = f"Квиз завершен!\n\nРезультат: {score} из {total}\nЗвание: {rank}"
    logging.info(f"Финиш юзера {message.chat.id}. Счет: {score}")
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=final_text)


# ЗАПУСК
if __name__ == "__main__":
    print("ООП Квиз-бот запущен...")
    bot.polling(none_stop=True)