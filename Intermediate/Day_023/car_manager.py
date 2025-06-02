from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self, width, height):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.width = int(width / 2)
        self.height = int(height / 2)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            y_position = random.randint(-(self.height - 50), (self.height - 50))
            new_car.goto(self.width, y_position)
            
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        for car in self.all_cars:
            car.backward(self.car_speed)
    
