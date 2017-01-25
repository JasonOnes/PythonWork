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
    #m = [(a, b) for a, b in num_list if (a + b) == sum_x]
    pairs_list = list()
    n = 0
    y = 1
    while n <= len(num_list) - 1:
        for x in num_list:
            if sum_x - num_list[n] == num_list[y]:
                pairs_list.extend([num_list[y], num_list[n]])
                y += 1
            n += 1
    print(pairs_list)
find_sum_pairs([1, 2, 3, 4, 5, 7], 7)
