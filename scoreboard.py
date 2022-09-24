from tkinter import Y
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.counter=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=270)
        self.goto(x=0,y=270) #because of undo command
    def score_on_screen(self):    
        self.undo()    
        self.write(f"Score: {self.counter}",align="center",font=["CHEDROS",12,"normal"])
    def game_over(self):
        self.goto(x=0,y=0)
        self.write("GAME OVER",align="center",font=["CHEDROS",18,"normal"])