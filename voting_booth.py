
def candidates(c=None):
    if c == None:
        c = list()

    x = input("Give me a list of names!: ")
    if x != 'done':
        c.append(x)
        print(c)
        candidates(c)

    elif x == 'done':
        print(c)

    return c

#candidates()
"""
def voting_booth():
    candidates_list = list()
    for voter in booth:
        candidates_list.append(candidates())
        print(candidates_list)
    cand_votes = {}
    cand_votes(enumerate(candidates_list))
    print(cand_votes)"""

def voting_booth(num_voters):
    cand_list = list()
    print("Welcome, step right up!")
    for voter in range(num_voters):
        print("Next!")
        cand_list.append(candidates())
    print(cand_list)
    return cand_list

voting_booth(5)

def election_results("county"):
    "county" = int(input("How many voters in the county? ")
    tally = dict(enumerate(set(voting_booth("county"))))
    print tally

election    
