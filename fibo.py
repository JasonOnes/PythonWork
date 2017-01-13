"""
Write a function that outputs a list of fibbonacci numbers.
Input is how many numbers to calculate.

>>> fibo(10)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

>>> fibo(20)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

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
    m = list(range(x))
    n = 0
    # f = [(num[n] + num[n+1]) for num in m ]
    for num in m:
        f = num[n] + num[n + 1]
        m.append(f)
        n += 2
    print(f)


fibo(7)


# sum of two preceding index numbers
def fibo_iterator(x):
    m = range(x)
    fib[n] == fib[n - 1] + fib[n - 2]

