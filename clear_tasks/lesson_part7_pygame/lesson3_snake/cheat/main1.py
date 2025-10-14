import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Определение цветов в формате RGB
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Задание размеров окна игры
dis_width = 800
dis_height = 600

# Создание окна игры
mw = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')  # Установка заголовка окна
clock = pygame.time.Clock()  # Создание объекта для управления временем

# Задание параметров змейки
snake_block = 10  # Размер одного блока змейки
snake_speed = 15  # Скорость игры (кадры в секунду)

# Создание шрифтов для отображения текста
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


# Функция для отображения счета
def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    mw.blit(value, [0, 0])  # Отображение счета в верхнем левом углу


# Функция для рисования змейки
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(mw, black, [x[0], x[1], snake_block, snake_block])  # Рисует каждый блок змейки


# Функция для отображения сообщений на экране
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mw.blit(mesg, [dis_width / 6, dis_height / 3])  # Центрирует сообщение на экране


# Основной игровой цикл
def gameLoop():
    game_over = False  # Переменная для отслеживания окончания игры
    game_close = False  # Переменная для отслеживания состояния "проигрыша"

    # Начальные координаты головы змейки
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0  # Изменение по оси X
    y1_change = 0  # Изменение по оси Y

    snake_List = []  # Список для хранения координат блоков змейки
    Length_of_snake = 1  # Начальная длина змейки

    # Генерация начальных координат еды
    foodx = round(random.randint(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randint(0, dis_height - snake_block) / 10.0) * 10.0


    while not game_over:  # Основной цикл игры
        while game_close == True:  # Цикл при проигрыше
            mw.fill(blue)  # Заполнение фона синим цветом
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)  # Сообщение о проигрыше
            Your_score(Length_of_snake - 1)  # Отображение счета
            pygame.display.update()  # Обновление экрана

            for event in pygame.event.get():  # Обработка событий
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Выход из игры при нажатии Q
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Повторная игра при нажатии C
                        gameLoop()

        for event in pygame.event.get():  # Обработка событий во время игры
            if event.type == pygame.QUIT:  # Закрытие окна игры
                game_over = True
            if event.type == pygame.KEYDOWN:  # Обработка нажатий клавиш
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block  # Движение влево
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block  # Движение вправо
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block  # Движение вверх
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block  # Движение вниз
                    x1_change = 0

        # Проверка выхода за границы окна
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Обновление координат головы змейки
        x1 += x1_change
        y1 += y1_change
        mw.fill(blue)  # Заполнение фона синим цветом

        # Рисование еды на экране
        pygame.draw.rect(mw, green, [foodx, foody, snake_block, snake_block])

        snake_Head = []  # Список для хранения координат головы змейки
        snake_Head.append(x1)  # Добавление текущих координат головы в список
        snake_Head.append(y1)
        snake_List.append(snake_Head)  # Добавление головы в общий список змейки

        # Удаление старого блока из списка, если длина змейки превышает заданную длину
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Проверка на столкновение с самой собой
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        draw_snake(snake_block, snake_List)  # Рисование змейки на экране
        Your_score(Length_of_snake - 1)  # Отображение счета

        pygame.display.update()  # Обновление экрана

        # Проверка на поедание еды
        if x1 == foodx and y1 == foody:
            foodx = round(random.randint(0, dis_width - snake_block) / 10.0) * 10.0  # Генерация новых координат еды
            foody = round(random.randint(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1  # Увеличение длины змейки

        clock.tick(snake_speed)  # Установка частоты обновления экрана

    pygame.quit()  # Завершение работы Pygame
    quit()  # Завершение программы


gameLoop()  # Запуск основного игрового цикла
