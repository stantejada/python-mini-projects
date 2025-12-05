from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Car
import time
from random import randint

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)


def main():

    player = Player()
    scoreboard = Scoreboard()
    car = Car()

    screen.listen()
    screen.onkeypress(player.move_up, "Up")

    dificulty = 0.9
    speed = 0.1

    running= True
    while running:
        time.sleep(speed)
        screen.update()

        car.move()

        #goal
        if player.ycor() > 280:
            scoreboard.next_level()
            player.refresh_player()
            speed *= dificulty

        for c in car.cars:
            if c.xcor() < -280:
                car.refresh_car(c)

            if c.distance(player) < 20:
                scoreboard.game_over()
                running = False

        


if __name__ == "__main__":
    app = main()
    screen.exitonclick()

