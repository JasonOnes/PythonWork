"""
Write a function that returns the meal for any given hour of the day.

Breakfast: 7AM - 9AM
Lunch: 12PM - 2PM
Dinner: 7PM - 9PM
Hammer: 10PM - 4AM

>>> meal(7)
'Breakfast time.'
>>> meal(13)
'Lunch time.'
>>> meal(20)
'Dinner time.'
>>> meal(21)
'Dinner time.'
>>> meal(0)
'No meal scheduled at this time.'
>>> meal(3)
'Hammer time.'
>>> meal(9999)
'Not a valid time.'


"""


def meal(time):
    """
    This is a funtion level docstring.
    Can also put doctests here.
    >>> meal(9)
    'Breakfast time.'
    """


    if time >= 24:
        message =  "Not a valid time."
    elif time in list(range(7, 10)):
        message = "Breakfast time."
    elif time in list(range(12, 15)):
        message = "Lunch time."
    elif time in list(range(19, 22)):
        message = "Dinner time."
    elif time >= 22 and time <= 24: #  Range didn't work out so well between,
    #  midnight an 4am
        message = "Hammer time."
    elif time >=1 and time <= 4:
        message = "Hammer time."
    else:
        message =  "No meal scheduled at this time."

    return message
