import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
import random
timmy = Turtle()
timmy.shape("turtle")


def colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


timmy.speed("fastest")


def spiro(size):
    for i in range(int(360/size)):
        timmy.color(colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+10)


spiro(2)


screen = Screen()
screen.exitonclick()