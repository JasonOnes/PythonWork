""" quick reminder about string manipulations and "appending" strings"""


def stringy_reversey(x):
    y = str()
    n = -1
    while abs(n) <= len(x):
        z = x[n]
        y += z
        n -= 1
    print(y)
    return y

stringy_reversey("Hey there, baby!")
