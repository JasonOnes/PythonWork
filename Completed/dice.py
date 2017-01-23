
import random
def roll():
    x = int(input("How many dice do you want to roll? "))
    y = int(input("What size die are you casting? "))
    roll = random.randint(1, x) * random.randint(1, y)
    print(roll)

roll()
