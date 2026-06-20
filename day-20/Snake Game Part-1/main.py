from turtle import Turtle,Screen
from snake import Snake
import time

screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(fun=snake.up ,key='Up')
screen.onkey(fun=snake.down ,key='Down')
screen.onkey(fun=snake.left ,key='Left')
screen.onkey(fun=snake.right ,key='Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()



screen.exitonclick()
