"""
# Given an input list, exclude an input integer and it's following element.
>>> exclude_em([56, 57, 58, 59, 60], 57)
[56, 59, 60]

>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34], 456)
[43, 67, 878, 5, 65, 34]


# Remove the first two element by default.
>>> exclude_em([43, 67, 456, 23, 878, 5, 65, 34])
[456, 23, 878, 5, 65, 34]



# Given two lists of ints, multiply numbers located at the same index
# in thier respective lists. If the reusult is zero, append -1 instead.
>>> double([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0])
[86, 67, 456, 46, 1756, -1, -1, -1]


# Given two lists and an int, insert the elements of a list into the first list at the nth position
>>> punch_in([43, 67, 456, 23, 878, 5, 65, 34], [2, 1, 1, 2, 2, 0, 0, 0], 2)
[43, 67, 2, 1, 1, 2, 2, 0, 0, 0, 456, 23, 878, 5, 65, 34]
"""

"""
def exclude_em(num_list, num):
    clean_list = list()
    for item in num_list:
        if item != num:
            clean_list.append(item)
        elif item == num:

"""
from operator import mul


def exclude_em(num_list, num=None):

    if num is None:
        return num_list[2:]

    if num in num_list:
        index = num_list.index(num)
        del num_list[index:index+2]
    elif num not in num_list:
        del num_list[:2]

    print(num_list)

#exclude_em([12, 2, 33, 65], 33)
#exclude_em([43, 364, 88, 2, 71], 22)

def double(num_list1, num_list2):
    double_list = list()
    zipped_list = zip(num_list1, num_list2)
    #print(zipped_list)
    for couplet in zipped_list:
        new_item = mul(*couplet)
        if new_item == 0:
            new_item = -1
        double_list.append(new_item)
    print(double_list)


#double([11, 32, 4, 667], [4, 3, 2, 8])

def punch_in(num_list1, num_list2, position):
    #big_new_list = num_list1.insert(num_list2, position)
    big_new_list = num_list1[:position] + num_list2 + num_list1[position:]
    print(big_new_list)


#punch_in([2, 3, 66, 9], [7, 11, 956, 55], 3)
