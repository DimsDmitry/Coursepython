from random import randint

import pygame


pygame.init()  # инициализация основных возможностей
pygame.font.init()  # подключаем шрифты

# заготовки для шрифтов
font_text = pygame.font.SysFont('bahnschrift', 40)
font_score = pygame.font.SysFont('comicsansms', 35)

def get_result():
    """открывает фаил с результатом, если его нет или он пуст - возвращает ноль"""
    with open('result.txt', 'r') as f:
        try:
            result = f.read()
            return int(result)
        except:
            return 0

def write_result(result: int):
    """открывает фаил с результатом, перезаписывает рекорд"""
    with open('result.txt', 'w') as f:
        try:
            f.write(str(result))
            print('Запись успешна')
        except:
            print('Ошибка записи результата')



class Button:
    """Класс кнопки"""
    def __init__(self, x, y, width, height, color):
        # создаём прямоугольник:
        self.rect = pygame.Rect(x, y, width, height)
        self.main_color = color

    def color(self, new_color):
        """красит в указанный цвет"""
        self.main_color = new_color

    def fill(self):
        # заливка прямоугольника цветом
        pygame.draw.rect(mw, self.main_color, self.rect)

    def set_text(self, text, fsize, text_color=(0, 0, 0)):
        # создаём объект шрифта
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)


    def draw(self, shift_x, shift_y):
        """рисуем прямоугольник с текстом и сдвигаем текст"""
        self.fill()
        if self.image:
            mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def collidepoint(self, x, y):
        """проверяет клик в конкретной точке, возвращает
        True или False, в зависимости от того в ту ли точку был клик"""
        return self.rect.collidepoint(x, y)


def draw_score(score, x, y):
    """отрисовывает текущий счёт игрока"""
    value = font_score.render('Ваш счёт: ' + str(score), True, YELLOW)
    mw.blit(value, [x, y])


def draw_snake(snake_block, snake_list):
    """принимает размер блока и список блоков змейки"""
    for x in snake_list:
        # далее этот список распаковывается и каждый квадрат змейки рисуется отдельно
        pygame.draw.rect(mw, BLACK, [x[0], x[1], snake_block, snake_block])


def draw_message(message, color, x, y):
    """выводит на экран сообщение указанного цвета"""
    text = font_text.render(message, True, color)
    mw.blit(text, [x, y])


# определяем цвета в формате RGB
WHITE = (255, 255, 255)
YELLOW = (255, 255, 108)
BLACK = (0, 0, 0)
RED = (230, 60, 60)
GREEN = (44, 255, 59)
BLUE = (94, 156, 255)

WIDTH, HEIGHT = 800, 600
mw = pygame.display.set_mode((WIDTH, HEIGHT))  # создаём экран

pygame.display.set_caption('Snake')  # заголовок

def game_loop():
    """функция запускающая основной игровой цикл"""
    # начальные координаты змейки - ровно центр экрана
    x1 = WIDTH // 2
    y1 = HEIGHT // 2

    # переменные, отслеживающие изменение координаты змейки
    x1_change = 0
    y1_change = 0

    # координаты еды
    food_x = randint(60, WIDTH-60)
    food_y = randint(60, HEIGHT-60)

    len_snake = 1  # длина змейки
    snake_list = []  # список для хранения координат блока змейки

    game_over = False  # флаг состояния всего игрового цикла
    game_stop = False  # флаг состояния игры

    clock = pygame.time.Clock()  # игровой таймер

    while not game_over:
        while game_stop:
            # если флаг игры включился - останавливаем игру, выводим кнопки выбора
            # продолжения или завершения игра
            mw.fill(BLUE)
            # выводим сообщение об окончании игры и счёте
            draw_message('Игра окончена!', RED, WIDTH / 2.8, HEIGHT / 2.9)
            best_result = get_result()  # получаем лучший результат предыдущей игры
            if len_snake - 1 > best_result:
                # проверяем, не побит ли рекорд. Если да - выводим сообщение об этом
                draw_message(f'Новый рекорд: {len_snake - 1}!', RED, WIDTH / 2.95, HEIGHT / 2.4)
                # перезаписываем рекорд в файл
                write_result(len_snake - 1)
            else:
                # если нет - выводим отдельно и рекорд
                draw_message(f'Ваш счёт: {len_snake - 1}', RED, WIDTH / 2.5, HEIGHT / 2.4)
                draw_message(f'Рекорд: {best_result}', RED, WIDTH / 2.4, HEIGHT / 2.05)

            # создаём две кнопки - перезапуска игра и выхода
            button_restart = Button(320, 350, 70, 40, WHITE)
            button_restart.fill()
            button_restart.set_text('Рестарт', 14)
            button_restart.draw(8, 10)

            button_stop = Button(420, 350, 70, 40, WHITE)
            button_stop.fill()
            button_stop.set_text('Выйти', 14)
            button_stop.draw(10, 10)

            """Обработка кликов по кнопке"""
            for event in pygame.event.get():
                # проверяем тип события
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # если нажата левая кнопка мыши - проверяем куда именно она попала
                    # (x, y) - кортеж с координатами клика. Распакуем его в две разные переменные
                    x, y = event.pos

                    # проверяем по какой кнопке сделан клик
                    if button_restart.collidepoint(x, y):
                        # клик по первой кнопке - перезапуск игры
                        game_loop()
                    if button_stop.collidepoint(x, y):
                        # клик по первой кнопке - конец игры
                        pygame.quit()  # корректно завершаем работу pygame



            pygame.display.update()
            clock.tick(20)


        # игра длится, пока game_over не равна True
        for event in pygame.event.get():  # получаем все события из внешнего мира
            # print(event)
            if event.type == pygame.QUIT:
                # обрабатываем событие QUIT, закрывающее окно - завершаем игру
                game_over = True
            if event.type == pygame.KEYDOWN:  # проверяем - нажата кнопка?
                # обработаем нажатие стрелок и перемещение вверх/вниз/влево/вправо
                if event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    y1_change = 0
                    x1_change = -10
                elif event.key == pygame.K_RIGHT:
                    y1_change = 0
                    x1_change = 10

        # если змейка достигла одной из границ экрана - она вылазит с противоположной
        if x1 >= WIDTH:
            x1 = 0
        elif x1 <= 0:
            x1 = WIDTH
        elif y1 >= HEIGHT:
            y1 = 0
        elif y1 <= 0:
            y1 = HEIGHT

        # запишем новые значения координат змейки
        x1 += x1_change
        y1 += y1_change

        mw.fill(BLUE)  # заливка экрана

        # каждый шаг цикла отрисовываем еду:
        pygame.draw.rect(mw, RED, pygame.Rect(int(food_x), int(food_y), 10, 10))
        # рамка для экрана:
        # pygame.draw.rect(mw, BLACK, pygame.Rect(10, 10, WIDTH-80, HEIGHT-20), 3)

        # создаём список, в котором будет храниться длина змейки в движении
        snake_head = [x1, y1]
        snake_list.append(snake_head)  # добавляем голову змейки в общий список

        # чтобы змейка не увеличивалась просто в движении, удаляем первый элемент в списке
        if len(snake_list) > len_snake:
            del snake_list[0]

        # анализируем, не столкнулся ли один из блоков змейки с головой
        # для этого сравним их координаты
        for x in snake_list[:-1]:
            if x == snake_head:
                # столкновение произошло - игра окончена
                game_stop = True

        draw_snake(10, snake_list)
        draw_score(len_snake-1, 10, 10)

        # проверяем столкновение змейки и еды
        if abs(x1 - food_x) < 10 and abs(y1 - food_y) < 10:
            # меняем координаты еды
            food_x = randint(60, WIDTH - 60)
            food_y = randint(60, HEIGHT - 60)
            len_snake += 1


        # в конце каждой итерации обновляем экран и устанавливаем частоту кадров в секунду
        pygame.display.update()
        clock.tick(20)

game_loop()
pygame.display.update()
