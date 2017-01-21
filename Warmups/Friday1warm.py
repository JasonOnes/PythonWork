import string

def pswrd_valid(x):
    check = list()
    for char in x:
        if ord(char) < 97:
            check.append(1)
        elif ord(char) > 97 and ord(char) < 122:
            check.append(1)
        elif char == int:
            check.append(1)
        elif char in string.punctuation:
            check.append(1)
        elif len(x) > 6 and len(x) < 12:
            check.append(1)

        check_sum = sum(check)

    if check_sum == 5:
        print("Valid")
        #return Valid
    else:
        print("Invalid")
        #return Invalid

pswrd_valid("jason1")
#pswrd_valid("Osgo56ww")
#pswrd_valid("wHa&2lll")
