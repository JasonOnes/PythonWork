"""
Implement solutions in as many ways as possible.

- Increment
- Enumertate
- Range
- For Each

>>> a = 'music'
>>> b = [17, 28, 42, 31, 12]

>>> display_indexes(a)
m 0
u 1
s 2
i 3
c 4


>>> parallel(a, b)
m 17
u 28
s 42
i 31
c 12

"""


def display_indexes_increment(x):
    m = 0
    for l in x:
        print(l, m)
        m += 1

def display_indexes_enumerate(x):
    for i, index in enumerate(x):
        print(i, index)


def display_indexes_range(x):
    for i in range(x):
        print(i)

def parallel_increment(x, y):
    for i, v in zip(x, y):
        print(i, v)

def parallel_enumerate(x, y):
    for i, v in enumerate(x, y):
        print(i, v)

def parallel_range(x, y):
    for i in range(x, y):
        print(i)




