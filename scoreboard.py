from turtle import Turtle
from food import Food
with open("data.txt") as data:
    data_high_score = int(data.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=data_high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High score: {self.high_score}", align="center", font=("Arial", 22, "normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score=0
        self.update_scoreboard()


    # def game_over(self):
        # self.goto(0,0)
        # self.write(f"Game Over.", align="center", font=("Arial", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()