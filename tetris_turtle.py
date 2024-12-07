"""
Tetris Tutorial using turtle library
By @TokyoEdTech
Youtube Channel: https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg
Video URL: https://youtu.be/JuMqaU_664k
"""
import random
import time
import turtle

COLORS = ["black", "cyan", "blue", "orange", "yellow", "lime", "blue violet", "red"]

wn = turtle.Screen()
wn.title("TETRIS by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0)

DELAY = 0.1

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 1, 2, 3, 0, 0, 0, 7, 4, 1, 2, 3],
]

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
# pen.setundobuffer(None)


class Shape:
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)

    def move_left(self, given_grid):
        if self.x > 0:
            if grid[shape.y][shape.x - 1] == 0:
                given_grid[shape.y][shape.x] = 0
                self.x -= 1

    def move_right(self, given_grid):
        if self.x < 11:
            if grid[shape.y][shape.x + 1] == 0:
                given_grid[shape.y][shape.x] = 0
                self.x += 1


def draw_grid(given_pen, given_grid):
    pen.clear()
    top = 230
    left = -110
    for y in range(len(given_grid)):
        for x in range(len(given_grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color = COLORS[given_grid[y][x]]
            given_pen.color(color)
            given_pen.goto(screen_x, screen_y)
            given_pen.stamp()


# Create a basic shape for the start of the game
shape = Shape()

# Put the shape in the grid
grid[shape.y][shape.x] = shape.color

# Draw the initial grid
draw_grid(pen, grid)
count = 0

wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "a")
wn.onkeypress(lambda: shape.move_right(grid), "d")

# Main game loop
game_over = False
while not game_over:
    wn.update()

    # Move the shape
    if shape.y == 23:
        shape = Shape()
    elif grid[shape.y + 1][shape.x] == 0:
        grid[shape.y][shape.x] = 0
        shape.y += 1
        grid[shape.y][shape.x] = shape.color
    else:
        shape = Shape()
        count += 1
        print(f"Making new Shape: {count}")

    # Check bottom row is full or not
    y = 23
    is_full = True
    for x in range(12):
        if grid[y][x] == 0:
            is_full = False
            break
    if is_full:
        for y in range(22, -1, -1):
            for x in range(12):
                grid[y + 1][x] = grid[y][x]

    draw_grid(pen, grid)
    time.sleep(DELAY)

wn.mainloop()