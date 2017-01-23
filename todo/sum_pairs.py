"""
Go through the search list and find all pairs of numbers that would add together to the sum.

>>> find_sum_pairs([-1, 0, 1, 2], 3)
[[1, 2]]

>>> find_sum_pairs([-1, 0, 1, 2], 1)
[[-1, 2], [0, 1]]

>>> find_sum_pairs([2, -1, 2], 1)
[[2, -1], [-1, 2]]

>>> find_sum_pairs([-1, 1, 2, 2], 3)
[[1, 2], [1, 2]]

"""

# Nested list comprehension perhaps?

def find_sum_pairs(num_list, sum_x):
    m = [(a, b) for a, b in num_list if (a + b) == sum_x]
    print(m)

find_sum_pairs([1, 2, 3, 4, 5, 7], 7)
