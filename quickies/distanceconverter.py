"""
Distance converts.
"""


def distance_convert():
    distance = int(input("How far? "))
    units = str(input("In what unit of measure? "))
    target = str(input("What do you want this converted to? "))
    if units == 'mi' and target == 'km':
        new_unit = distance * 1.6094
    elif units == 'mi' and target == 'feet':
        new_unit = distance * 5280
    elif units == 'mi' and target == 'm':
        new_unit = distance * 1609.34
    elif units == 'km' and target == 'mi':
        new_unit = distance * 0.621371
    elif units == 'km' and target == 'feet':
        new_unit = distance * 3280.84
    elif units == 'km' and target == 'm':
        new_unit = distance * 1000
    elif units == 'feet' and target == 'mi':
        new_unit = distance * 0.000189394
    elif units == 'feet' and target == 'km':
        new_unit = distance * 0.0003048
    elif units == 'feet' and target == 'm':
        new_unit = distance * 0.3048
    elif units == 'm' and target == 'mi':
        new_unit = distance * 0.000621371
    elif units == 'm' and target == 'km':
        new_unit = distance * 0.001
    elif units == 'm' and target == 'feet':
        new_unit = distance * 3.28084
    else:
        print("Not valid input!")



    print("{} {} is {} in {}".format(distance, units, new_unit, target))

distance_convert()
