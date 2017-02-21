""" more review list iteration"""

def product(x):
    #y = len(x)
    #import pdb; pdb.set_trace()
    n = 0
    total = 1
    while n <= len(x) -1:
        total = total * x[n]
        print(total)
        n += 1

    print(total)

product([2, 3, 1, 4])
