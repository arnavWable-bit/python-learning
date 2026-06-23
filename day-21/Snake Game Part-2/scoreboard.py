from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0
        with open("day-21/Snake Game Part-2/data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",move= False, align= ALIGNMENT, font=FONT)
        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day-21/Snake Game Part-2/data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False,align=ALIGNMENT, font= FONT)