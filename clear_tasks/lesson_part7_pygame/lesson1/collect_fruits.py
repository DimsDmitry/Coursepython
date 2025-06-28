import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Собери фрукты")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Персонаж
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

# Фрукты
fruit_size = 30
fruit_pos = [random.randint(0, WIDTH - fruit_size), 0]
fruit_speed = 10

# Очки
score = 0
font = pygame.font.SysFont("monospace", 35)

# Главный цикл игры
running = True
while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление персонажем
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 10

    # Обновление позиции фрукта
    fruit_pos[1] += fruit_speed

    # Проверка на сбор фрукта
    if (player_pos[1] <= fruit_pos[1] < player_pos[1] + player_size and
            player_pos[0] <= fruit_pos[0] < player_pos[0] + player_size):
        score += 1
        fruit_pos = [random.randint(0, WIDTH - fruit_size), 0]

    # Если фрукт выходит за пределы экрана
    if fruit_pos[1] > HEIGHT:
        fruit_pos = [random.randint(0, WIDTH - fruit_size), 0]

    # Отрисовка персонажа и фрукта
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (fruit_pos[0], fruit_pos[1], fruit_size, fruit_size))

    # Отображение очков
    score_text = font.render("Очки: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Обновление экрана
    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()