"""Parking lot inventory?"""


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


class ParkingLot:

    def __init__(self, capacity, hourly_rate):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.spaces = list()
        self.available_spaces = capacity


    def __str__(self):
        string = "There's {0.available_spaces} much room.".format(self)
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

    def leave(slef, vehicle):
        if vehicle in ParkingLot:
            self.available_spaces.pop(vehicle)
        return self



P_LOT = ParkingLot(capacity=7, hourly_rate=18)

def dropping_off():
    #cap = int(input("How many space are in this lot? >> "))
    #rate = input("Hourly price in Bitcoin.  >> ")

    print("Welcome to our lot:")
    plate = input("My car's plate# is: ")
    vehicle = Vehicle(plate=plate)
    P_LOT.park(vehicle)
    print(P_LOT.available_spaces)

def picking_up():
    plate = input("What is your plate #?  ")

    vehicle = Vehicle(plate=plate)
    #P_LOT.
    #lot = ParkingLot(capacity=cap, hourly_rate=rate)

    #lot.park(vehicle)
    if vehicle in spaces:
        print("Here it is!")
        print("Here's your bill {0.hourly_rate}".format(self))
    #self.available_spaces += 1
    #else:
    #    print("No {0.car} here.".format(self))

def run():#maybe have lot name as parameter
    response = input("Are you here to pick up or drop off?  ")
    if response == "drop off":
        dropping_off()
    elif response == "pick up":
        picking_up()
    else:
        print("Get off my driveway, ya Drunk!")


run()

        #self.capacity -= 1
