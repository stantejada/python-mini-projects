from turtle import Turtle, Screen
from random import randint


class Competitor(Turtle):
    def __init__(self, color, speed):
        super().__init__()
        self.color(color)
        self.speed(speed)
        self.shape("turtle")
        self.penup()


def main():

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("Racing turtle")



    red = Competitor("red", 5)
    blue = Competitor("blue", 5)
    green = Competitor("green", 5)


    #Starting positions
    red.goto(-350,100)
    blue.goto(-350,0)
    green.goto(-350,-100)

    competitors = [red, blue, green]

    finish = False

    while not finish:
        for c in competitors:
            move = randint(1,10)
            c.forward(move)
            if c.xcor() >= 350:
                finish = True

                print(f"{c.pencolor().capitalize()} wins!")
                break


    screen.exitonclick()


if __name__ == "__main__":
    main()

    