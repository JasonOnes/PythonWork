"""
write a function that performs this transformation

>>> shorten('horse')
'h3e'

>>> shorten('duck')
'd2k'

>>> shorten('student')
's5t'
"""


def shorten(x):
    r = str(len(x) - 2)
    m = (x[0] + r + x[-1])
    return m



