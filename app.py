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

# import random

# for i in range(10000000):
#     number = random.random()
#     number *= 200
#     number = round(number)
#     t.forward(number)
#     number = random.random()
#     number *= 360
#     number = round(number)
#     t.left(number)


# length = 100
# for i in range(10000000000):
#     t.forward(length)
#     t.speed(10000000)
#     t.left(144)
#     if i % 5 == 0:
#         length += 5
#         t.left(5)
# """ 
# def oddoreven(input):
#     if input % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# oddoreven(67) """
t.speed(10000000000000)
length = 0
for i in range(60):
    length += 5
    for i in range(3):
        t.forward(length)
        t.left(90)
    t.left(5)

tipoptions = [0, 15, 20, 25, 100]
serviceoptions = ["bad", "okay", "good", "great", "phenomenal"]

def tipfunction(bill, service):
    tip = "nothing"
    for i in serviceoptions:
        if i == service:
            tip = tipoptions[serviceoptions.index(i)]
    if tip == "nothing":

        while True:
            service = input("What?")
            breakloop = False
            for i in serviceoptions:
                if i == service:
                    tip = tipoptions[serviceoptions.index(i)]
                    breakloop = True
            if breakloop:
                break

    
    print("paid amount:", bill)
    print("service:", service)
    print("tip:", tip, "%")
    total = float(bill) + float(bill)*float(tip)*0.01

    print("total:", total)


bill = input("Input bill.")
bill = float(bill)

service = input("How was the service?")

tipfunction(bill, service)

