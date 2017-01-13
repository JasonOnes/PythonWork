
""" Cost to paint wall."""
import math

def paint_cost():

    width = int(input("How wide is the wall?: "))
    height = int(input("How high is the wall?: "))
    price = int(input("How much does the paint you want cost per gallon?: "))
    coats = int(input("How many coats?: "))
    one_gallon = 400
    x = width * height
    wall_one_gallons = math.ceil((coats * x) / 400)

    #cost = coats * ((x / 400) * price)
    cost = wall_one_gallons * price
    #print("It will cost ${} to paint your wall.".format(int(cost)))
    print("It will cost ${} to paint your wall.".format(int(cost)))
    print("You will need {} gallons for that wall.".format(wall_one_gallons))
    y = input("Want an estimate for another wall?: ")
    if y == "Yes":
        paint_cost()
    else:
        print("Have a good one!")

paint_cost()
