from turtle import Turtle 

class Gameball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("sircle")
        self.color("white")
        self.penup()
        self.goto(position)

