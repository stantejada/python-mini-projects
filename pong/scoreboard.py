from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        self.penup()
        self.goto(0,250)
        self.hideturtle()
        self.color("white")
        self.write(f"{self.player_2} - {self.player_1}", 24, font=FONT, align=ALIGMENT)

    def update_score(self):
        self.clear()
        self.goto(0,250)
        self.write(f"{self.player_2} - {self.player_1}", 24, font=FONT, align=ALIGMENT)