from random import randint
from turtle import Turtle
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

COLORS = ["orange","blue","yellow","black","green","red"]

def create_car(car_length: int, position: tuple) -> [Turtle]:
    turtles = []
    x_pos = position[0]
    car_color = random.choice(COLORS)
    for i in range(car_length):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color(car_color)
        segment.setposition(x=x_pos, y=position[1])
        segment.setheading(LEFT)
        turtles.append(segment)
        x_pos -= MOVE_DISTANCE
    return turtles

class Car:
    def __init__(self, starting_length: int, position: tuple, max_coords: tuple):
        self.segments = create_car(starting_length, position)
        self.head = self.segments[0]
        self.original_coords = self.get_coords()
        self.max_x = max_coords[0]
        self.max_y = max_coords[1]

    def get_coords(self) -> [tuple]:
        coords: [tuple] = []
        for segment in self.segments:
            coords.append(segment.pos())
        return coords

    def move_forward(self):
        for segment in self.segments:
            segment.forward(MOVE_DISTANCE)

    def new_location(self):
        increment = random.randint(0, 30)
        randomizer = random.choice([-1, 0, 1])
        for segment in self.segments:
            current_x = segment.xcor()
            current_y = segment.ycor()
            segment.goto((current_x + increment*randomizer, current_y + increment*randomizer))

    def back_to_start(self):
        for segment in self.segments:
            segment.goto(segment.pos()[0] + self.max_x * 2, segment.pos()[1])