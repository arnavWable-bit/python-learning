from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        self.goto(-280, 250)
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg= f"Level: {self.level}",align= 'left' ,move=False, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",align="center" ,font= ("Courier", 30, "normal"))