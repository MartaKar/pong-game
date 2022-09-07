from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.resizemode("user")
        self.penup()
        self.turtlesize(stretch_len=1, stretch_wid=5)
        self.goto(xcor, ycor)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)