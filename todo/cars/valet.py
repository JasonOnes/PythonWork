"""Parking lot inventory?"""


class Vehicle:

    def __init__(self, color, plate):
        self.color = color
        self.plate = plate

    def __str__(self):
        string = "The {0.color} with {0.plate} plate number.".format(self)
        return string

    def __repr__(self):
        rep = x
        return rep


class ParkingLot:

    def __init__(self, capacity, rate):
        self._capacity = capacity
        self.rate = rate
        self.spaces = list()
        self.available_spaces = capacity


    def __str__(self):
        string = "There's {0.available_spaces} much room.".format(self)
        return string

    def __repr__(self):
        pass


    def park_in(self, vehicle):
        if len(self.spaces) < self.capacity:
           self.spaces.append(vehicle)
           self.available_spaces -= 1
        else:
           print("Full!")
           return False

    #def car_left(self, vehicle):
    #    if vehicle


        #self.capacity -= 1
