""" Format string of numbers"""


def formater(x):
    cleanx = str(x)
    y = list()
    for num in cleanx:
        #if num == int:
            y.append(num)
    if len(cleanx) % 2 == 0:
        z = len(cleanx) / 2

    elif len(cleanx) != 0:
        z = int((len(cleanx)) / 2 + 0.5)
    #print(z)
    section_1 = y[:z]
    section_2 = y[z:]

    print(section_1)
    print(section_2)
    section_1A = (''.join(section_1))
    section_2A = (''.join(section_2))

    #section_2A.join("-")
    print(section_1A)
    print(section_2A)
    section_1B = section_1A
    section_2B = section_2A[1:] + '-' + [::3]
    print(section_2B)
formater(922323454)
