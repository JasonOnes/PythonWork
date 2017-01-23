def fancy_phone():
    x = list(input("Please enter your phone number: "))
    #if len(x) == 10:
        #for item in range(x(0,4)):

    x.insert(0, '(')
    x.insert(4, ')' )
    x.insert(8, '-' )
    # y = str(x)
    y = ''.join(x)
    print(y)

fancy_phone()
