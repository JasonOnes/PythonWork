"""
Work on creating functions for each choice
"""




def phonebook(p_book=None):
    if p_book is None:
        p_book = dict()

    x = input("Do you want to: \n1. create a new contact\n"
              "2. Retrieve and existing contact\n"
              "3. Update a contact\n"
              "4. Delete a contact\nor \'quit\'\n")
    if x == "1":
        handle = input("What's your handle partner? ")
        real_name = input("And your real name? ")
        age = input("How old are you {}? ".format(handle))
        number = input("What's your number? ")
        p_book[handle] = real_name, age, number

        print(p_book)
        #phonebook(p_book=p_book)
    elif x == "2":
        handle = input("Who are you trying to find? ")
        y = p_book[handle]
        print(y)
        #phonebook(p_book=p_book)
    elif x == "3":
        y = input("What contact do you want to change? ")
        """if y in p_book:
            pass
        elif y not in p_book:
            print("I don't recognize that handle!\n Try again.")
        """
        z = input("What do you want to change?\n1.{}'s real name?\n2.{}'s age?\n3.{}'s number?".format(y))
        if z == "1":
            new_name = input("What do you want to change name to? ")
            p_book[y] = new_name
            #change name, del old and replace with new?
        elif z == "2":
            new_age = input("How old is {} really? ".format(handle))
            #change age
        elif z == "3":
            new_number = input("What's their actual number? ")
            #change number
        else:
            print("Nice try!")
        p_book[y] = z
        print(p_book)

    elif x == "4":
        handle = input("What contact do you want to delete? ")
        del p_book[handle]
        print(p_book)
        #phonebook(p_book=p_book)
    elif x == "quit":
        quit()

    phonebook(p_book=p_book)



phonebook()

