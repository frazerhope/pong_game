from turtle import Turtle
import time

LINE_LENGTH = 80
SCREEN_WIDTH = 800


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0

        self.scoreboard()
        self.center_line()

    def scoreboard(self):

        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.score()
    def score(self):
        self.write(f'{self.score_1}                     {self.score_2}', align='center', font=('Arial', 30, 'normal'))

    def center_line(self):
        centerline = Turtle()
        centerline.color('white')
        centerline.shape('square')
        centerline.shapesize(0.25,3)
        centerline.penup()
        centerline.goto(0, 370)
        centerline.setheading(270)
        for _ in range(0, int(SCREEN_WIDTH/LINE_LENGTH)):
            centerline.stamp()
            centerline.forward(LINE_LENGTH+40)

    def add_score_1(self):
        self.clear()
        self.score_1 += 1
        self.score()

    def add_score_2(self):
        self.clear()
        self.score_2 += 1
        self.score()
