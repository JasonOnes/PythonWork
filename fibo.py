"""
Write a function that outputs a list of fibbonacci numbers.
Input is how many numbers to calculate.

>>> fibo(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

>>> fibo(20)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]d

>>> fibo(30)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


Write a Generator function named 'fib_infinite()' to calculate fibbonacci numbers to infinity.
>>> fibo_iterator = fib_infinite()
>>> next(fib_infinite)
0
>>> next(fib_infinite)
1
>>> next(fib_infinite)
1
>>> next(fib_infinite)
2
>>> next(fib_infinite)
3
>>> next(fib_infinite)
5
>>> next(fib_infinite)
8
>>> next(fib_infinite)
13
"""



def fibo(x):
    f = list([0])
    num = 0
    num_b = 1
    # f = [(num[n] + num[n+1]) for num in m ]
    while num < x:
        num, num_b = num_b, num + num_b
        #num_b = num + num_b
        print(num)
        f.append(num)

    print(f)
    #print(f[-1])

#fibo(7)

def largest_fibo(x):
    #fibo(x)
    print(fibo[x][-1])

largest_fibo(7)


class Fibo(object):
    def __init__(self):
        self = self
        #self.num = self + num

    def next(self):
        new_self = fibo(self)
        print(new_self)

    
