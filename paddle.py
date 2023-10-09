from turtle import Turtle

PADDLE_INITIAL_POSITION_1 = (-340,0)
PADDLE_INITIAL_POSITION_2 = (340,0)


class Paddle(Turtle):
    def __init__(self,paddle_number):
        super().__init__()
        self.paddle_number = paddle_number
        self.paddle_generator()

    def paddle_generator(self):
        if self.paddle_number == 1:
            PADDLE_INITIAL_POSITION = PADDLE_INITIAL_POSITION_1
        else:
            PADDLE_INITIAL_POSITION = PADDLE_INITIAL_POSITION_2

        self.shape('square')
        self.shapesize(1, 5)
        self.color('white')
        self.penup()
        self.setheading(90)
        self.goto(PADDLE_INITIAL_POSITION)



        # for position in range(0, PADDLE_WIDTH):
        #
        #     paddle_piece = Turtle(shape='square')
        #     paddle_piece.penup()
        #     paddle_piece.color('white')
        #     paddle_piece.goto(PADDLE_INITIAL_POSITION[position])
        #     self.paddle_objects.append(paddle_piece)

    # control functions


    def up(self):
        self.setheading(90)
        self.forward(30)

    def down(self):
        self.setheading(270)
        self.forward(30)



