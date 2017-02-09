def is_prime(x):
    if x < 2:
        return False
    elif x == 2 or x == 3:
        return True
    for num in range(2,(x-1)):
        if x % num == 0:
            print("False")
            return False
            num += 1
    else:
        print("True")

is_prime(9)
