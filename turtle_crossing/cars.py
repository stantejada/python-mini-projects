from turtle import Turtle
from random import choice, randint
from scoreboard import Scoreboard

import time


COLORS = ["red", "blue", "brown", "yellow", "orange"]

class Car:
    def __init__(self):

        self.cars = []

        self.random_y()


    def random_y(self):
        for _ in range(25):
            new_y = randint(-200,200)
            new_x = randint(-200,200)
            self.create_car(new_x, new_y)



    def create_car(self, x, y):
        new_car = Turtle()
        new_car.shape("square")
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.setheading(180)
        new_car.color(choice(COLORS))
        new_car.goto(x, y)
        self.cars.append(new_car)
            

    def move(self):
        car = choice(self.cars)
        car.forward(25)

    def refresh_car(self, c):
        y = randint(-200,200)
        c.goto(280, y)

