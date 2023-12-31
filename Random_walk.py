# Making the turtle to move in random directions with different colors or bold width with the help of turtle graphics documentation.

from turtle import Turtle
import random
import turtle

tim = Turtle()

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

draw_spirograph(5)        

screen = turtle.Screen()
screen.exitonclick()