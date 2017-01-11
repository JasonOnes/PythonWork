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
    indices_list = list()
    for l in word:
        if l == word[range(0,-1,1)]:
            indices_list + word[n]

        print(indices_list)
        return indices_list

