from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')

        self.goto(0,0)
        self.start_random_move()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def start_random_move(self):
        random_angle = random.randint(0,270)
        self.setheading(random_angle)

    def reflection_collision(self):
        heading = self.heading()
        angle_of_reflection = 360-heading
        self.setheading(angle_of_reflection)

    def paddle_bounce(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.paddle_bounce()