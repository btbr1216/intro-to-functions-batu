import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

# t.forward(200)

# turtle.done()

# def double(one, two):
#     print(one)
#     print(two)
# double(6, 7)

# rangee = 0


# def turn(number, shapee, side):

#     turnamt = 0
#     if shapee == "square":
#         turnamt = 90
#     elif shapee == "triangle":
#         turnamt = 120
    
#     if side == "left":
#         t.backward(number)
#         if upsidedown:
#             t.left(turnamt)
#         else:
#             t.right(turnamt)
#     else:
#         t.forward(number)
#         if upsidedown:
#             t.right(turnamt)
#         else:
#             t.left(turnamt)


# shapee = "triangle"
# size = 200
# side = "left"
# upsidedown = True



# if shapee == "square":
#     rangee = 4
# elif shapee == "triangle":
#     rangee = 3

# for i in range(rangee):
#     turn(size, shapee, side)

import random

for i in range(10000000):
    number = random.random()
    number *= 200
    number = round(number)
    t.forward(number)
    number = random.random()
    number *= 360
    number = round(number)
    t.left(number)


# length = 100
# for i in range(10000000000):
#     t.forward(length)
#     t.speed(10000000)
#     t.left(144)
#     if i % 5 == 0:
#         length += 5
#         t.left(5)

