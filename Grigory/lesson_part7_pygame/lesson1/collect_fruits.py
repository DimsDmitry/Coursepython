import pygame
from random import randint

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Собери фрукты")

# цвета
# RED = 'crimson'
RED = (255, 48, 33)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Персонаж
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

# Фрукты
fruit_size = 30
fruit_pos = [randint(0, WIDTH), 0]
fruit_speed = 10

# Счётчики
pygame.font.init()
score = 0
font = pygame.font.SysFont('monospace ', 35)

clock = pygame.time.Clock()  # таймер

# Игровой цикл
run = True
while run:
    screen.fill(WHITE)  # заливка экрана
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            # если нажата кнопка выход - завершаем игру
            run = False
    # Управление персонажем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 10
    elif keys[pygame.K_RIGHT]:
        player_pos[0] += 10

    # Обновление позиции фрукта
    fruit_pos[1] += fruit_speed

    # Проверка, собран ли фрукт
    if (player_pos[1] <= fruit_pos[1] < player_pos[1] + player_size and
            player_pos[0] <= fruit_pos[0] < player_pos[0] + player_size):
        # Если координаты игрока и фрукта совпали - прибавляем очко
        score += 1
        # И создаём фрукту новые координаты
        fruit_pos = [randint(0, WIDTH), 0]

    # Если фрукт вышел за пределы экрана, тоже создаём новый фрукт
    if fruit_pos[1] > HEIGHT:
        fruit_pos = [randint(0, WIDTH), 0]

    # Отрисовка персонажа и фрукта
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (fruit_pos[0], fruit_pos[1], fruit_size, fruit_size))

    # отображение очков
    score_text = font.render('Очки: ' + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # обновление экрана
    pygame.display.update()
    clock.tick(30)

pygame.quit()