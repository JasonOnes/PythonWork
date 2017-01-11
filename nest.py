"""
>>> LETTERS
[['a', 'b', 'c'], ['d', 'e', 'f', 'g'], ['h', 'i']]

>>> denest()
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
"""

LETTERS = [['a', 'b', 'c'],
           ['d', 'e', 'f', 'g'],
           ['h', 'i']]

def denest():
    m = list()
    for item in LETTERS:
        m += item
    return m

#x = ['asldfkj', 'jjjjj', 'kkkk']
#denest(x)

