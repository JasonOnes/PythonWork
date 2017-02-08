""" binary search"""
import random


def guess():

    maximum = 4 * (10**7)
    minimum = 1
    comp_guess = maximum // 2
    x = random.randint(1, maximum)            # computers choice

    count = 1
    while comp_guess != x:

        if comp_guess > x:
            maximum = comp_guess
            comp_guess = (minimum + maximum) // 2
            count += 1
            print(comp_guess, count)
            continue

        elif comp_guess <  x:
            minimum = comp_guess
            comp_guess = (minimum + maximum) // 2
            count += 1
            print(comp_guess, count)
            continue

    if comp_guess == x:
        print("Got it!!")



guess()
