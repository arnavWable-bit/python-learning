import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move()
    
    
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.increase_speed()
    
    # Detect car collision 
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()