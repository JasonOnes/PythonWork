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
"""
def find_sum_pairs(num_list, sum_x):
    #m = [(a, b) for a, b in num_list if (a + b) == sum_x]
    pairs_list = list()
    first_index = 0
    second_index = 1
    while first_index <= len(num_list) - 1:
        for taco in num_list:
            #while second_index < len(num_list):
            if sum_x - num_list[first_index] == num_list[second_index]:
                pairs_list.extend([num_list[first_index], num_list[second_index]])
                second_index += 1
            #elif sum_x - num_list[first_index] != num_list[second_index]:
                #second_index += 1
            first_index += 1
    print(pairs_list)

find_sum_pairs([1, 2, 3, 4, 5, 7], 7)

def find_sum_pairs(num_list, sum_x):
    pairs_list = list()
    for number in num_list:
        if number + num_list[-1] == sum_x:
            pairs_list.append([number, num_list[-1]])
        num_list[-1] -= num_list[1
    print(pairs_list)

find_sum_pairs([1, 2, 3, 4, 5, 7], 7)
"""

# Still doesn't pass all the doctests but O(1), I think
def find_sum_pairs(num_list, sum_x):
    pairs_list = list()
    first_index = 0
    second_index = -1
    sorta_listing = sorted(num_list)
    for num in num_list:
        if sorta_listing[first_index] + sorta_listing[second_index] > sum_x:
            second_index -= 1
        elif sorta_listing[first_index] + sorta_listing[second_index] < sum_x:
            first_index += 1
        elif sorta_listing[first_index] + sorta_listing[second_index] == sum_x:
            pairs_list.extend([sorta_listing[first_index], sorta_listing[second_index]])
            first_index += 1
    print(pairs_list)

find_sum_pairs([1, 2, 3, 4, 5, 7], 7)
