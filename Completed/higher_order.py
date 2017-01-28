"""
>>> numbers = [2, -4, -6, 7,-9, 1, 9, -2, -3, 6]

>>> sorted_absolute(numbers)
[1, 2, -2, -3, -4, -6, 6, 7, -9, 9]

>>> quote = "In the end, it's concluded that the airspeed velocity of a (European)\
 unladen swallow is about 24 miles per hour or 11 meters per second. But, the real \
 question is not about swallows at all."

>>> shortest_to_longest(quote)
['a', 'In', 'of', 'is', '24', 'or', '11', 'is', 'at', 'the', 'the', 'per', 'per', 'the', 'not', 'end,', "it's", 'that', 'hour', 'But,', 'real', 'all.', 'about', 'miles', 'about', 'meters', 'unladen', 'swallow', 'second.', 'airspeed', 'velocity', 'question', 'swallows', 'concluded', '(European)']

>>> sort_last_char(quote)
['(European)', 'end,', 'But,', 'second.', 'all.', '11', '24', 'a', 'concluded', 'airspeed', 'the', 'the', 'the', 'of', 'real', 'In', 'unladen', 'question', 'per', 'hour', 'or', 'per', "it's", 'is', 'miles', 'meters', 'is', 'swallows', 'that', 'about', 'not', 'about', 'at', 'swallow', 'velocity']

>>> double(numbers)
[4, -8, -12, 14, -18, 2, 18, -4, -6, 12]

>>> all_upper(quote)
['IN', 'THE', 'END,', "IT'S", 'CONCLUDED', 'THAT', 'THE', 'AIRSPEED', 'VELOCITY', 'OF', 'A', '(EUROPEAN)', 'UNLADEN', 'SWALLOW', 'IS', 'ABOUT', '24', 'MILES', 'PER', 'HOUR', 'OR', '11', 'METERS', 'PER', 'SECOND.', 'BUT,', 'THE', 'REAL', 'QUESTION', 'IS', 'NOT', 'ABOUT', 'SWALLOWS', 'AT', 'ALL.']

>>> positive(numbers)
[2, 7, 1, 9, 6]

Filter words longer than 3, make all words lowercase words, and sort by last letter.
>>> lower_last_longwords(quote)
['(european)', 'end,', 'but,', 'second.', 'all.', 'concluded', 'airspeed', 'real', 'unladen', 'question', 'hour', "it's", 'miles', 'meters', 'swallows', 'that', 'about', 'about', 'swallow', 'velocity']
    m = [(i * 2) for i in x]
    return m

def sort_last_char(x):
    y = x.split()
    m = sorted(y, key=lambda word: word[-1])
    return m

def positive(x):
    m = list()
    for i in x:
        if i > 0:
            m.append(i)
    return m

def shortest_to_longest(x):
    new_list = x.split()
    new_list.sort(key=len)
    return new_list

def all_upper(x):
    m = x.upper().split()
    return m

def lower_last_longwords(x):
    y = x.lower().split()