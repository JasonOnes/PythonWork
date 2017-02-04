from datetime import datetime


class Vehicle:

    def __init__(self, plate, color=None):
        self.color = color
        self.plate = plate

    def __str__(self):
        string = "The {0.color} with {0.plate} plate number.".format(self)
        return string

    def __repr__(self):
        rep = x
        return rep

class Ticket:

    def __init__(self, space_num, time=datetime.datetime):
        self.space_num = space_num
        self.time = datetime.datetime


class ParkingLot:

    def __init__(self, name, capacity, hourly_rate):
        self.name = name
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.spaces = list()
        self.available_spaces = capacity


    def __str__(self):
        string = "{0.format} has {1.format} and costs{2.formtat}.".format(self)
        return string

    def __repr__(self):
        pass

    def park(self, vehicle):
        if len(self.spaces) < self.capacity:
           self.spaces.append(vehicle)
           self.available_spaces -= 1
           return self
        else:
           print("Full!")
           return False

    def leave(self, vehicle):
        if vehicle in ParkingLot:
            self.available_spaces.pop(vehicle)
        return self


JacksSpaces = ParkingLot(capacity=17, hourly_rate=18)
