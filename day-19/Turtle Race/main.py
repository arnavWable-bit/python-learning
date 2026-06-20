from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=900)
user_bet = screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-239,y=-100)

Y= -200
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-380,y=Y )
    Y += 80

if user_bet:
    is_race_on = True
    
while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                
        steps = random.randint(0,10)
        turtle.forward(steps)
        
    










screen.exitonclick()    
