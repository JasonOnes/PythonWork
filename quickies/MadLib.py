#print("How many {} are in the {}?".format(input("Give me a number: "),
    #                                      input("Give me a noun: ")))
#  Keep parameters in line for format.

noun = input("Give me a noun, please: ")
adj = input("How 'bout an adjective: ")
verb = input("And a verb: ")
number = input("Now can I have a number: ")
number2 = input("How about another number: ")
measure = input("How big of a load: ")

print("So, there's this {} and it's really {}.\nLike a {} on a scale of 1 to {}."\
    "\nAnd {} likes to {} a lot. \nI mean a {} load.".format(noun, adj, number, number2,
       noun, verb, measure))

"""def MadLib():
    inputs = input("Give me a noun:", "Give me an adjective: ",
                   "Give me a number: ")
    print("So, there's this {} {} and it's {} years old.".format(inputs))

MadLib()
"""
