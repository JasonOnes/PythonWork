""" Given three ints return True if one of the list is close (differing by other
    two by at most 1) AND the other is far (>2 or more).
    """


def close_call(x):
    #x = tuple(a, b ,c)
    y = False
    z = False
    if (abs(x[1] - x[0]) <= 1 or abs(x[1] - x[2]) <=1) or
        abs(x[0] - x[2] <= 1):
        y = True
    if (abs(x[1] - x[0]) > 1 or abs(x[1] - x[2]) > 1) or
        abs(x[0] - x[2] > 1):

#if abs(x[0] - x[1]) > 1 or abs(x[0] - x[2]) > 1:
        z = True
    print(y and z)
    return y and z

x = [1, 2, 10]
close_call(x)

x = [1, 2, 3]
close_call(x)

x = [4, 1, 3]
close_call(x)

x = [4, 11, 34]
close_call(x)
