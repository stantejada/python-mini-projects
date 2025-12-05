from turtle import Turtle



class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=self.x, y=self.y)
    
    def up(self):
        self.y = self.ycor() + 20
        self.goto(x=self.x, y=self.y)
    
    def down(self):
        self.y = self.ycor() - 20
        self.goto(x=self.x, y=self.y)
