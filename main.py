from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(n=0)

# object initialisation

score = Score()
ball = Ball()

paddle_1 = Paddle(1)
paddle_2 = Paddle(2)

screen.listen()

screen.onkeypress(paddle_1.up, key='w')
screen.onkeypress(paddle_1.down, key='s')

screen.onkeypress(paddle_2.up, key='Up')
screen.onkeypress(paddle_2.down, key='Down')
screen.update()
speed = 0.1
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(speed)
    ball.move()

    if ball.xcor() > 380:
        score.add_score_1()
        ball.reset_position()
        speed = 0.1
    elif ball.xcor() < -380:
        score.add_score_2()
        ball.reset_position()
        speed = 0.1
    if ball.distance(paddle_1) < 60 and ball.xcor() < -320:
        print('made contact')
        ball.paddle_bounce()
        speed *= 0.95
    if ball.distance(paddle_2) < 60 and ball.xcor() > 320:
        print('made contact')
        ball.paddle_bounce()
        speed *= 0.95
    # wall collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
