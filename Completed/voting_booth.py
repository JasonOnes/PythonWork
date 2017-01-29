""" A very very simple voting program. Needs some tweaking to avoid multiple votes.
"""


from collections import Counter

def candidates(c=None):
    if c == None:
        c = list()
        ctr = Counter(c)

    x = input("Give me a list of names!: ")
    if x != 'done':
        c.append(x)
        print(c)
        ctr = Counter(c)
        print(ctr.most_common())
        candidates(c)
    elif x == 'done':
        print(c)
    return c

def voting(num_voters):
    num_voters = int(input("How many voters are there? "))
    big_list = list()
    for voter in range(num_voters):
        tally = candidates()
        print("=" * 25)
        big_list.extend(tally)

    print(Counter(big_list))

voting(4)
