from turtle import *

speed(20)
width(5)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)         #house
forward(200)
left(90)

forward(70)
color("red")
begin_fill()
left(90)
forward(120)   #door and its color
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

penup()
color("green")
begin_fill()
right(150)
forward(200)  #the roof and its color   
left(120)
forward(200)
end_fill()
pendown()

penup()
left(150)
left(150)
left(90)
forward(80)
left(90)
pendown()

penup()
color("yellow")
begin_fill()  
forward(45)  #the window and its color
left(90)
forward(45)
left(90)
forward(45)
end_fill()
pendown()

penup()
goto(200,200)
pendown()

penup()
left(90)
forward(80)
pendown()

penup()
begin_fill()
right(90)
forward(45)
right(90)
forward(45)
right(90)
forward(45)
end_fill()
pendown()









exitonclick()