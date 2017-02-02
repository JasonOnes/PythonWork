class Vehicle(object):
    def __init__(self, color, plate, doors):
        self.color = color
        self.plate = plate
        self.doors = doors

    def __str__(self):
        string = "{0.color} {0.doors} door #{0.plate}".format(self)
        return string

    def honk(self):
        #print("HONK!")
        return 'HONK!'
