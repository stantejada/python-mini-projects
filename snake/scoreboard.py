from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto((0,260))
        self.hideturtle()
        self.update_score()
       
        
    def update_score(self):
        self.write(f"Score: {self.score}", font = FONT , align=ALIGMENT)

    def game_over(self):
        self.goto((0,0))
        self.write("Game Over!", font = FONT , align=ALIGMENT)


    def score_add(self):
        self.clear()
        self.score += 1
        self.update_score()

