import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

# t.forward(200)

# turtle.done()

def double(one, two):
    print(one)
    print(two)
double(6, 7)

def turn(number, shapee, side):

    turnamt = 0
    if shapee == "square":
        turnamt = 90
    elif shapee == "triangle":
        turnamt = 120
    
    if side == "left":
        t.forward(-number)
        t.left(-turnamt)
    elif True:
        t.forward(number)
        t.left(turnamt)



shapee = "triangle"
size = 200
side = "right"



rangee = 0
if shapee == "square":
    rangee = 4
elif shapee == "triangle":
    rangee = 3

for i in range(rangee):
    turn(size, shapee, side)
