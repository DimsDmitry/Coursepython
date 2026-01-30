import turtle

# Создание окна и настройка размеров
wn = turtle.Screen()
wn.title('Игра с черепашками')
wn.bgcolor('lightblue')
wn.setup(width=600, height=600)

# Создание черепашек
turtle1 = turtle.Turtle()
turtle1.color('red', 'green')
turtle1.shape('turtle')
turtle1.speed('slowest')
turtle1.penup()
turtle1.goto(-300, -300)

turtle2 = turtle.Turtle()
turtle2.color('red', 'green')
turtle2.shape('turtle')
turtle2.speed('slowest')
turtle2.penup()
turtle2.goto(300, -300)


# Движение черепашек
def move_turtles():
    global turtle1, turtle2
    turtle1.forward(10)
    turtle2.forward(10)


# Проверка столкновений
def check_collisions():
    global turtle1, turtle2
    if turtle1.xcor() + 100 > turtle2.xcor():
        turtle1.right(90)
    else:
        turtle1.left(90)


# Основной цикл игры
while True:
    move_turtles()
    check_collisions()

wn.mainloop()
