"""
Write a function to return a list of integers
indicating the index of each letter occourance in a given test string.

>>> locate('l', 'hello')
[2, 3]

>>> locate('b', 'bannanas')
[0]

>>> locate('i', 'mississippi')
[1, 4, 7, 10]
"""


def locate(letter, word):
    m = list()
    n = 0
    d = len(word)
    while n < d:
        if letter == word[n]:
            m.append(n)
        n += 1
    print(m)

locate('b', 'alibaba')

