import random

def magic_ball():
    answers = ["Whateva!", "Nope!", "You wish!", "Sure, why not?"]
    print("Welcome to the 8-Ball of Death!")
    answer = input("Would you like to ask a question?(Y/N): ")
    x = answer.upper()
    if x == 'Y':
        print(input("What is your question? " ))
        print(random.choice(answers))
    else:
        print("See ya!")

    answer_2 = input("Would you like to ask another?(Y/N) ")
    y = answer_2.upper()
    if y == 'Y':
        magic_ball()
    else:
        print("Okay!")

magic_ball()
