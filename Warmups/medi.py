"""find the median value in a list"""


def median(x):
    y = sorted(x)
    l = len(y)

    if l % 2 == 0:
        z = (y[(l//2)] + y[(l//2)-1]) / 2

    else:
        n = l // 2
        z = y[n]

    print(z)
    return z

median([4, 5, 5, 4])
