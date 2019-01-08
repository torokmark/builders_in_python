#!/usr/bin/env python

class Car:
    def __init__(self, wheel=4, seat=4, color='red'):
        self.wheel = wheel
        self.seat = seat
        self.color = color

    def __str__(self):
        return '[wheels: {}, seats: {}, color: {}]'.format(self.wheel, self.seat, self.color)

class Builder:
    def set_wheels(self, wheel): pass
    def set_seats(self, seat): pass
    def set_color(self, color): pass

class CarBuilder(Builder):

    def __init__(self):
        self.car = Car()

    def set_wheels(self, wheel):
        self.car.wheel = wheel

    def set_seats(self, seat):
        self.car.seat = seat

    def set_color(self, color):
        self.car.color = color

    def get_result(self):
        return self.car

class CarBuilderDirector:
    def build(self):
        builder = CarBuilder()
        builder.set_wheels(8)
        builder.set_seats(4)
        builder.set_color("Red")
        return builder.get_result()
  
if __name__ == '__main__':
    car = CarBuilderDirector().build()
    print(car)
