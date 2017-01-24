"""
Use the zip() function!

>>> together('knights', 'camalot')
k c
n a
i m
g a
h l
t o
s t
"""

def together(x, y):
    #z = list()
    x = list(x)
    y = list(y)
    z = zip(x, y)
    for a, b in z:
        print(a, b)
    #print(z)
"""
x = 'knights'
y = 'camalot'
together(x, y)
"""
