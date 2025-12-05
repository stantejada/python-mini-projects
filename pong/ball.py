from turtle import Turtle
from random import choice




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.create_ball()
        self.pos_x = 10
        self.pos_y = 10

    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def move(self):
        new_x = self.xcor() + self.pos_x * self.speed
        new_y = self.ycor() + self.pos_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.pos_y *= -1

    def bounce_x(self):
        self.pos_x *= -1

    def refresh(self):
        self.clear()
        self.create_ball()
