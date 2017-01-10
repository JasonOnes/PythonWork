"""
# Return the Sum of two or less elements:
>>> combine_two(7, 4)
11

>>> combine_two(42)
42

# Return the sum of any number of integers
>>> combine_many(980, 667, 4432, 788, 122, 9, 545, 222)
7765

# Return the longest string
>>> choose_longer("Greg", "Rooney")
'Rooney'
"""



def combine_two(x, y=0):
    return x + y

def combine_many(*args):
    x = args
    m = 0
    for i in x:
        m = m + i

    return m

def choose_longer(x, y):
    if len(x) > len(y):
        return x
    elif len(x) < len(y):
        return y
    else:
        return None


