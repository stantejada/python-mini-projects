from turtle import Screen
import time
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle(350,0)
player_2 = Paddle(-350,0)
scoreboard = Scoreboard()
ball = Ball()

screen.listen()
screen.onkeypress(player_1.up, "Up")
screen.onkeypress(player_1.down, "Down")
screen.onkeypress(player_2.up, "w")
screen.onkeypress(player_2.down, "s")

def main():
    running = True

    while running:
        time.sleep(0.1)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.xcor() > 400:
            scoreboard.player_2 += 1
            scoreboard.update_score()
            ball.refresh()
        
        if ball.xcor() < -400:
            scoreboard.player_1 += 1
            scoreboard.update_score()
            ball.refresh()

        #Detect collision with paddle player 1
        if ball.distance(player_1) < 50 and ball.xcor() > 320 or ball.distance(player_2) < 50 and ball.xcor() > -320:
            ball.bounce_x()
        
        
        


    screen.exitonclick()


if __name__ == "__main__":
    app=main()