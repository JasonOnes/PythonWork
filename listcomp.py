"""
>> square_routes
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> square_halves
[2, 8, 18, 32, 50]

>>> NAMES
['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> long_names(5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with('S')
['Suki', 'Serada']

>>> PEOPLE
[('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> first_names(PEOPLE)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(PEOPLE)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""


PEOPLE = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]
NAMES = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

squares = [(i**2) for i in range(1, 11)]
#here's the troubles
square_halves = [int(i / 2) for i in squares if i % 2 == 0]



def long_names(n):
    #m = list()
    #if len(i) in NAMES >= n:
     #   m += i
    m = [i for i in NAMES if len(i) >= n]
    return m

def starts_with(l):
    #m = list()
    #if i[0] in NAMES == l:
     #   m += i
    m = [i for i in NAMES if i[0] == l]
    return m

def first_names(x):
    #m = list()
    return [i[1] for i in x]

def smoosh(x):
    m = list()
    for i in x:
        m.extend(i)
    return m



