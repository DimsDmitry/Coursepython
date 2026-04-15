import telebot
from telebot import types
import logging  # для логов

from key import KEY

# запускаем логгирование:
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='helper2_bot.log',
    filemode='a',
    encoding='utf-8'
)

# инициализируем бота, передаём в него токен (ключ доступа)
bot = telebot.TeleBot(KEY)

class Question:
    """класс для создания вопросов, хранит в себе сам вопрос и список ответов"""
    def __init__(self, text, options):
        self.text  = text  # Текст вопроса
        self.options = options  # Список кортежей с вариантами ответа [('Ответ1', 'Ответ2')]

    def create_keyboard(self, index):
        """Метод класса для создания собственной клавиатуры"""
        markup = types.InlineKeyboardMarkup()
        for opt_text, status in self.options:
        # создаём callback_data, в него передаём индекс вопроса и статус ответа
            callback_data = f'{index}_{status}'
            # передаём их в клавиатуру
            markup.add(types.InlineKeyboardButton(opt_text, callback_data=callback_data))
        return markup

# Создание списка объектов.
# Каждый элемент списка - экземпляр класса Question
QUIZ_DATA = [
    Question('Какой язык мы сейчас изучаем?', [('Python', 'correct'), ('Java', 'wrong'), ('C++', 'wrong')]),
    Question('Что такое объект?', [('Набор свойств и методов', 'correct'), ('Набор функций', 'wrong')]),
    Question('Можно ли сочетать операторы "and" и "or" в одном условии?', [('Да', 'correct'), ('Нет', 'wrong')]),
    Question('Для чего нужно логирование?', [('Для отслеживания работы', 'correct'), ('Для красоты', 'wrong')]),
    Question('Как называется метод-конструктор класса в Python?', [('__init__', 'correct'), ('__str__', 'wrong')])
]


score = 0  # глобальный счётчик ответов


# Шаг 1 - запуск квиза (обработчик команды /start)
@bot.message_handler(commands=['start'])
def start_quiz(message):
    """Функция срабатывает при команде /start"""
    global score
    score = 0
    logging.info(f'Пользователь {message.from_user.first_name} начал квиз.')  # логгируем событие - начало квиза
    # берём самый первый объект вопроса из списка
    question1 = QUIZ_DATA[0]
    # отправляем пользователю сообщение с вопросом
    bot.send_message(
        message.chat.id,
        f'❓Вопрос №1: {question1.text}',
        reply_markup=question1.create_keyboard(0)
    )
    # reply_markup привязывает к сообщению клавиатуру




# Шаг 2 - обработка нажатий
@bot.callback_query_handler(func=lambda call: True)
# "слушатель" кнопок - если кнопка нажата возвращает True (принимает нажатие любой кнопки)
def handle_quiz(call):
    global score  # указываем переменную глобальной

    # разбираем данные из нажатой кнопки
    data_parts = call.data.split('_')
    cur_index = int(data_parts[0])  # индекс - целое число
    status = data_parts[1]  # статус вопроса - строка

    # проверка корректности, вывод пользователю соответствующего сообщения
    if status == 'correct':
        score += 1  # ответ верный - плюс 1 к счётчику
        bot.answer_callback_query(call.id, 'Правильно!✅')
    else:
        bot.answer_callback_query(call.id, 'Неверно!❌')
    next_index = cur_index + 1  # переходим к след. объекту вопроса
    # проверяем, не закончились ли вопросы:
    if next_index < len(QUIZ_DATA):
        # если проверка пройдена, берём следующий объект из списка:
        question_next = QUIZ_DATA[next_index]
        # редактируем сообщение под новый вопрос
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f"❓Вопрос №{next_index + 1}: {question_next.text}",
            reply_markup=question_next.create_keyboard(next_index)
        )
        # передаём индекс текущего вопроса + 1 (например индекс вопроса 1, значит он 2-й по порядку)
    else:
        # если вопросы закончились, переводим на функцию для отображения результатов
        show_result(call.message)

# Шаг 3 - ФИНАЛ (отображение результатов)
def show_result(message):
    """Рассчитывает результат игрока на основе набранных баллов"""
    total = len(QUIZ_DATA)  # определяем макс. кол-во баллов, оно равно кол-ву вопросов
    if score == total:
        result = 'Профи'
    elif score == total - 1:
        result = 'Опытный'
    elif score == 1 or score == 2:
        result = 'Новичок'
    elif score == 0:
        result = 'Неопытный джун'
    else:
        result = 'Средний'

    logging.info(f'Пользователь {message.chat.id}. Счёт: {score}')
    text = f"Квиз завершён!\n\nТвой результат: {score} из 5.\nЗвание: {result}\nНажми /start чтобы начать заново!"
    bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text=text)

# Запуск бота!
if __name__ == '__main__':
    print('Квиз-бот запущен...')
    bot.polling(none_stop=True)