from turtle import Turtle

MOVE_DISTANCE = 20

class Crosser(Turtle):
    def __init__(self, y_position):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.sety(y_position)

    def move_up(self):
        current_y = self.ycor()
        self.sety(current_y + MOVE_DISTANCE)

    def move_down(self):
        current_y = self.ycor()
        self.sety(current_y - MOVE_DISTANCE)

    def move_left(self):
        current_x = self.xcor()
        self.setx(current_x - MOVE_DISTANCE)

    def move_right(self):
        current_x = self.xcor()
        self.setx(current_x + MOVE_DISTANCE)

    def back_to_start(self, position):
        self.setpos(position)