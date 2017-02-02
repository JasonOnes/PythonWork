"""Parking lot inventory?"""


class Vehicle(self):

    def __init__(self, color, plate):
        self.color = color
        self.plate = plate

    def __str__(self):
        string = "The {0.color} with {0.plate} plate number.".format(self)
        return string

    def __repr__(self):
        rep = x
        return rep


class ParkingLot(self):

    def __int__(self, capacity, rate):
        self.capacity = capacity
        self.rate = rate
        self.spaces = list()
    def __str__(self):
        string = "There's {0.capacity} much room."
        return string

    def __repr__(self):
        rep = something
        return rep


    def park_in(self, vehicle):
        if len(self.spaces) < self.capacity:
           self.spaces.append(vehicle)
       else:
           print("Full!")
           return False

    def car_left(self, vehicle):
        if vehicle


        #self.capacity -= 1
