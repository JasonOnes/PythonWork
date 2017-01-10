"""
Here are the rules for the FizzBuzz problem:

Given the length of the output of numbers from 1 - n:
If a number is divisible by 3, append "Fizz" to a list.
If a number is divisible by 5, append "Buzz" to that same list.
If a number is divisible by both 3 and 5, append "FizzBuzz" to the list.
If a number meets none of theese rules, just append the string of the number.

>>> fizz_buzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']


REMEMBER: Use Encapsulation! D.R.Y.
>>> joined_buzz(15)
'1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz'

"""


def fizz_buzz(x):
    y = list()
    for i in range(1, x + 1):

        if i % 15 == 0:
            y.append("FizzBuzz")
        elif i % 3 == 0:
            y.append("Fizz")
        elif i % 5 == 0:
            y.append("Buzz")
        else:
            y.append(str(i))
    return y

def joined_buzz(x):
    y = " ".join(fizz_buzz(x))
    return y


