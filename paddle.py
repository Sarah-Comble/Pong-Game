from turtle import Turtle


class Paddle(Turtle) :

    def __init__(self, position) :
        super().__init__()
        # paddle = Turtle()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
