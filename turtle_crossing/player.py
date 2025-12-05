from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.shapesize(stretch_wid=1.5, stretch_len= 1.5)
        self.penup()
        self.goto(0,-250)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def refresh_player(self):
        self.goto(0,-250)
