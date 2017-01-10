"""
1. Slice off the last digit.
That is the **check digit**.
1. Reverse the digits.
1. Double every other element in the reversed list.
1. Subtract nine from numbers over nine.
1. Sum all values.
1. Take the second digit of that sum.
1. If that matches the check digit, the whole card number is valid.

For example, the worked out steps would be:

1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
1. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
1. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
1. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
1. 85
1. 5
1. Valid!


>>> validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])
Valid!

>>> validate([6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4])
Invalid!


"""

def validate(account_number):
   """Write your code here"""


   check_digit = account_number.pop()
   account_number.reverse()
   # m = list()

   for i in range(0, len(account_number)):
      even_acct_num = account_number[i % 2 == 0]
      odd_acct_num = account_number[i % 2 != 0]
      new_acct_num = even_acct_num + odd_acct_num
      #if account_number[i % 2] == 0:
         # account_number[i] *= 2
#account_number[i] is giving the value at that index
      if even_acct_num:
         return even_acct_num * 2
      if odd_acct_num:
         return odd_acct_num
      if account_number[i] > 9:
         account_number[i] -= 9

   fresh_number = sum(new_acct_num)
   digits = str(fresh_number)

   if digits[1] == check_digit:
      print("Valid!")
   else:
      print("Invalid!")

   return None

validate([4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5])