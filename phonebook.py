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
        contact = input("What's your handle partner? ")
        real_name = input("And your real name? ")
        age = input("How old are you {}? ".format(contact))
        number = input("What's your number? ")
        p_book[contact] = real_name, age, number

        print(p_book)
        #phonebook(p_book=p_book)

    elif x == "2":
        handle = input("Who are you trying to find? ")
        if handle in p_book:
            print(p_book[handle])
        else:
            print("Sorry, no such contact.")
        #print(y)
        #phonebook(p_book=p_book)

    elif x == "3":
        contact = input("What contact do you want to change? ")
        if contact in p_book:
            #continue
        #elif contact not in p_book:
        #    print("I don't recognize that handle!\n Try again.")

            change = input("What do you want to change?\n1.{0}'s real name?\n2.{0}'s age?\n3.{0}'s number?".format(contact))

            # Lookup existing person and find thier real name.

            if change == "1":
                new_name = input("What do you want to change name to? ")
                p_book[contact][real_name] = new_name
                #change name, del old and replace with new?
            elif change == "2":
                new_age = input("How old is {} really? ".format(contact))
                p_book[age] = new_age
            elif change == "3":
                new_number = input("What's their actual number? ")
                p_book[number] = new_number
            else:
                print("Nice try!")
        elif contact not in p_book:
            print("I don't recognize that handle!\n Try again.")

        p_book[contact] = new_name
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
