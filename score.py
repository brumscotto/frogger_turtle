from turtle import Turtle

FONT = ("arial", 20, "normal")

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.setpos(position)
        self.update_level()

    def increase_level(self):
        self.level += 1
        self.update_level()

    def update_level(self):
        self.clear()
        # self.showturtle()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.showturtle()
        self.setpos(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
