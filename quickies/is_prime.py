def is_prime(x):
    if x >= 0 and x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    for num in range(2,(x-1)):
        if x % num == 0:
            #num += 1
            print("False")
            return False
            num += 1
        #elif  x % num != 0:
        #    num += 1
        #    print("True")
        #    return True
        else:
            print("True")

is_prime(9)
