""" binary search"""
import random


def guess():

    #maximum = 4_000_000_000
    maximum = 4 * (10**7)
    comp_guess = maximum // 2
    #a = int in range(1, comp_guess)
    #b = int in range(comp_guess, maximum)
    x = random.randint(1, maximum)            # computers choice
    #comp_guess = random.randint(1, maximum)
                 #  2bill
    #half = x / 2

    count = 1
    while comp_guess != x:

        if comp_guess > x:
            comp_guess = comp_guess - (maximum - comp_guess) // 2
            count += 1
            print(comp_guess)
            continue

        elif comp_guess <  x:
            comp_guess = comp_guess + (maximum -comp_guess) // 2
            count += 1
            print(comp_guess)
            continue

    if comp_guess == x:
        print("Got it!!")



guess()
