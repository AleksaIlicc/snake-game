from turtle import Turtle, position
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.all_snake_parts=[]
        self.create_snake()
        self.head=self.all_snake_parts[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        
    def move(self):
        for snake_part in range(len(self.all_snake_parts)-1,0,-1):
            newxcor=self.all_snake_parts[snake_part-1].xcor()
            newycor=self.all_snake_parts[snake_part-1].ycor()
            self.all_snake_parts[snake_part].goto((newxcor,newycor))
        self.head.forward(20)
    def add_segment(self,position):
        turtle=Turtle()
        turtle.shape('square')
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.all_snake_parts.append(turtle)

    def extend(self):
        self.add_segment(self.all_snake_parts[-1].position())



    #snake can"t go reverse mode
    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:   
            self.head.setheading(270)
    def left(self):   
        if self.head.heading()!=0:
            self.head.setheading(180)
    def right(self):   
        if self.head.heading()!=180:
            self.head.setheading(0)