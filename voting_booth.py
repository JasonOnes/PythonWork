
def candidates():
    candidates = []
    x = input("Give me a list of names!: ")
    while x != 'done':
        candidates.append(x)
    elif x == 'done':
        print("Finally")
    print(candidates)
    return candidates

candidates()
