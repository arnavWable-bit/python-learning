# import colorgram

# colors = colorgram.extract(
#     "day-18/The Hirst Painting Project/hirstimage.jpg",
#     30
# )

# rgb_colors = []

# for color in colors:
#     my_tuple = (color.rgb.r,color.rgb.g,color.rgb.b)
#     rgb_colors.append(my_tuple)
    

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")

color_list = [(253, 253, 252), (241, 244, 247), (241, 249, 246), (251, 246, 249), (140, 78, 53), (187, 164, 121), (52, 111, 136), (164, 153, 39), (19, 44, 78), (143, 59, 84), (138, 167, 176), (62, 119, 100), (143, 183, 173), (81, 34, 28), (218, 210, 97), (65, 153, 168), (111, 39, 32), (97, 146, 117), (167, 98, 129), (100, 122, 168), (169, 147, 163), (31, 53, 107), (179, 102, 84), (110, 37, 48), (74, 33, 42), (206, 183, 195), (171, 202, 191), (18, 99, 83), (170, 200, 203), (11, 96, 112)]

tim.hideturtle()
tim.penup()
tim.goto(-250, -250)

def row():
    for _ in range(10): 
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)

def back_and_up(row):
    y = -250 + row * 50
    tim.goto(-250,y)

for i in range(1,11):
    row()
    back_and_up(i)

screen = t.Screen()
screen.exitonclick()