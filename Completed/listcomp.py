"""
>> squares
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> square_halves
[2, 8, 18, 32, 50]

>>> names
['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> long_names(5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with('S')
['Suki', 'Serada']

>>> people
[('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> first_names(people)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""
names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']
people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

squares = [(i ** 2) for i in range(11)]
square_halves = [int(i / 2) for i in squares if i != 0 and i % 2 == 0]


def long_names(x):
    #m = list()
    m = [i for i in names if len(i) >= x]
    print(m)

def starts_with(x):
    m = [i for i in names if i[0] == x]
    return m

def first_names(x):
    m = [i[1] for i in x]
    return m


def smoosh(x):
    m = [i for i in (x[0] + x[1] + x[2])]
    return m

