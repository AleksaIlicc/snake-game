from tkinter import Y
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.goto(x=0, y=270)  # because of undo command
        with open("E:\Py\snake-game\data.txt") as rfile:
            self.highscore=int(rfile.read())

    def score_on_screen(self):
        self.undo()
        self.write(f"Score: {self.score}    High Score:{self.highscore}", align="center",
                   font=["CHEDROS", 15, "normal"])

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("E:\Py\snake-game\data.txt",mode="w") as file:
                file.write(str(self.highscore))
            
        self.score=0

    # def game_over(self):
    #     self.goto(x=0,y=0)
    #     self.write("GAME OVER",align="center",font=["CHEDROS",18,"normal"])
