import random
import time
from turtle import Turtle,Screen
from car import Car
from crosser import Crosser
from score import Score

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
LAST_LANE_LINE_Y = SCREEN_HEIGHT / 2 - 60
game_speed_s = 0.1

def create_background():
    lane_line = Turtle(shape="square")
    lane_line.pensize(2)
    lane_line.hideturtle()
    lane_line.color("black")
    lane_line.penup()

    starting_x = (SCREEN_WIDTH / 2) - 50
    ending_x = -SCREEN_WIDTH / 2 + 50
    y_pos = LAST_LANE_LINE_Y

    lane_line.setpos(starting_x,y_pos)
    lane_line.setheading(180)
    road_height = 40
    lanes = int(SCREEN_HEIGHT//road_height) - 2

    for _ in range(lanes):
        while lane_line.pos()[0] > ending_x:
            lane_line.pendown()
            lane_line.forward(20)
            lane_line.penup()
            lane_line.forward(20)
        y_pos -= road_height
        lane_line.setpos(starting_x,y_pos)


def check_crossing_status():
    global game_speed_s
    crosser_y = crosser.ycor()
    if crosser_y > LAST_LANE_LINE_Y + 20:
        score.increase_level()
        crosser.back_to_start((0, int(-SCREEN_HEIGHT//2) + 20))
        relocate_cars(level_cars)
        level_cars.extend(arrange_cars(5))
        time.sleep(1)
        game_speed_s *= 0.75
        return False
    return True

def create_new_car() -> Car:
    max_x = int(SCREEN_WIDTH // 2) - 50
    max_y = int(SCREEN_HEIGHT // 2) - 50
    new_car_len = random.randint(2, 4)
    new_car_coords = (random.randint(-max_x, max_x),
                      random.randint(-max_y, max_y))
    new_car = Car(new_car_len, new_car_coords, (max_x, max_y))
    return new_car

def arrange_cars(num_cars: int) -> [Car]:
    cars: [Car] = []
    for i in range(num_cars):
        new_car = create_new_car()
        cars.append(new_car)
    return cars

def move_cars(cars: [Car]):
    for car in cars:
        if car.segments[len(car.segments)-1].xcor() < - SCREEN_WIDTH // 2:
            car.back_to_start()
        else:
            car.move_forward()

def relocate_cars(cars: [Car]):
    for car in cars:
        car.new_location()

def check_for_contact(t: Turtle, cars: [Car]):
    for car in cars:
        for segment in car.segments:
            if t.distance(segment.pos()) < 20:
                return False
    return True

screen = Screen()
screen.tracer(False)

screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("white")
screen.title("Turtle Crossing")

starting_cars = 15

create_background()
level_cars = arrange_cars(starting_cars)

score = Score((-SCREEN_WIDTH/2 + 20,SCREEN_HEIGHT/2 - 30))
starting_y_position = int(-SCREEN_HEIGHT//2) + 20
crosser = Crosser(starting_y_position)

screen.listen()

screen.onkey(key="Up",fun=crosser.move_up)
screen.onkey(key="Down",fun=crosser.move_down)
screen.onkey(key="Right",fun=crosser.move_right)
screen.onkey(key="Left",fun=crosser.move_left)

is_playing = True

while is_playing:
    screen.update()
    move_cars(level_cars)
    is_playing = check_for_contact(crosser,level_cars)
    check_crossing_status()
    time.sleep(0.25)
score.game_over()

screen.exitonclick()
