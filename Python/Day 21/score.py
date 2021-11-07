from turtle import Turtle

FONT = ("Arial", 10, "normal")
ALIGN = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()

    def update(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
    def inc(self):
        self.score += 1
        self.clear()
        self.update()