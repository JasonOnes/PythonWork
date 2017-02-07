""" mask a string with #### except last 4 characters"""


def string_mask(x):
    y = list()
    for chars in x[:-4]:
        y.append("#")
    c = y + list(x[-4:])
    print(c)

x = ('1234')
string_mask(x)

x = ('123456789')
string_mask(x)
