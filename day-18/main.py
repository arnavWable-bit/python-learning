#from turtle import Turtle,Screen
import turtle as t
import random

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)


# MAKING A SQUARE
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)



# MAKING A DASHED LINE
# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.color("white")
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.color("black")


# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()



# DRAWING DIFF SHAPES

# colors = [
#     "red",
#     "tomato",
#     "gold",
#     "lime",
#     "cyan",
#     "dodgerblue",
#     "magenta",
#     "violet"
# ]

# def draw_shapes(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides): 
#         timmy_the_turtle.forward(50)
#         timmy_the_turtle.right(angle)


# for shape_side_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shapes(shape_side_n)




# GENERATE A RANDOM WALK

# direction = [0,90,180,270]

# timmy_the_turtle.pensize(10)

# for _ in range(100):
#     timmy_the_turtle.color(random.choice(colors))
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.setheading(random.choice(direction))



# TUPLE AND GENERATE RANDOM RGB COLORS

# my_tuple = (1,3 ,8)
# print(my_tuple[0])

# my_tuple[2] = 12                  # Tuples are immutable 

# print(list(my_tuple))

t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_color = (r,g,b)
    return random_color



# direction = [0,90,180,270]

# timmy_the_turtle.pensize(10)
timmy_the_turtle.speed('fastest')

# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.setheading(random.choice(direction))


# DRAW A SPIROGRAPH

def draw_spirograph(size_of_gap): 
    for _ in range(int(360/size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)
        
draw_spirograph(5) 






screen = t.Screen()
screen.exitonclick()