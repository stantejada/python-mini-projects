from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

snake  = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def main():

    running = True

    while running:
        time.sleep(0.1)
        screen.update()
        snake.move()

        #Detect collision with food
        if snake.head.distance(food) < 15:
            scoreboard.score_add()
            snake.extend()
            food.refresh()

        #Detect Collision with wall
        if snake.head.xcor() > 380 or snake.head.xcor() < -400 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
            scoreboard.game_over()

            running = False

        #Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                running = False
                scoreboard.game_over()
    
    screen.exitonclick()

if __name__ == "__main__":
    app = main()
