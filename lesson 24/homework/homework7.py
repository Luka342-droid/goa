import turtle

def draw_square(x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

turtle.setup(800, 800)
turtle.speed(5)

draw_square(-300, 100, 200)
draw_square(100, 100, 200)
draw_square(-300, -300, 200)
draw_square(100, -300, 200)

turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()
turtle.forward(800)

turtle.penup()
turtle.goto(0, -400)
turtle.setheading(90)
turtle.pendown()
turtle.forward(800)

turtle.hideturtle()
turtle.done()
