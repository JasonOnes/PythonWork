"""
Given an input list, return it in reverse.
>>> backwards([56, 57, 58, 59, 60])
[60, 59, 58, 57, 56]


Find the max number in a given list.  Then, change every element in the list containing the first number of the maximum to the maximum number.
>>> maximus([56, 57, 58, 59, 60])
[60, 57, 58, 59, 60]

>>> maximus([56, 67, 56, 59, 60])
[67, 67, 67, 59, 67]


Given two lists, return True of the first two items are the equal.
>>> compare_first_element(['migratory', 'birds', 'fly', 'south'], ['migratory', 'monopoloy', 'mind'])
True

Return True if the first letter of the second element in the list is the same. (case insensitive)
>>> compare_second_letter(['migratory', 'penguins', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
True

>>> compare_second_letter(['migratory', 'birds', 'fly', 'south'], ['One', 'Pound', 'Coconut'])
False


Given two lists, return one list, with all of the items of the first list, then the second
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'])
['mama', 'llama', 'baba', 'yaga']


Use a default argument to allow the user to reverse the order!
>>> smoosh(['mama', 'llama'], ['baba', 'yaga'], reverse=True)
['yaga', 'baba', 'llama', 'mama']


"""

def backwards(list_x):
    list_x.reverse()
    return list_x


def maximus(list_x):

    biggest = max(list_x)
    big_num = list(str(biggest))[0]
    big = str(big_num)

    list_y = list()
    for element in list_x:
        if big in str(element):
            list_y.append(biggest)
        else:
            list_y.append(element)

    return list_y

def compare_first_element(list_x, list_y):
    if list_x[0] == list_y[0]:
        return True
    else:
        return False

def compare_second_letter(list_x, list_y):
    # str(list_x).lower()
    # str(list_y).lower()
    #list_y.lower(str(list_y))
    # second_x = list(list_x)[1][0]
    # second_y = list(list_y)[1][0]
    if list_x[1][0].lower() == list_y[1][0].lower():
        return True
    else:
        return False
"""
cars = ['datsun', 'suzuki', 'honda']
trucks = ['ford', 'saturn', 'toyota']
compare_second_letter(cars, trucks)
"""

def smoosh(list_x, list_y, reverse=False):
    list_x.extend(list_y)
    if reverse is True:

        list_x.reverse()
        return list_x
    #list_x.extend(list_y)
    return list_x

    #return list_x.extend(list_y)

