""" given a list of at least 3 int values return sum.
    If one of the values is 13 then it doesn't count or the the values
    following. If 13 is first value return 0.
    """


def list_sum_no_thirteen(x):
    sum_list = list()
    for num in x:
        if num != 13:
            sum_list.append(num)
        elif x[0] == 13:
            return 0
        elif num == 13:
            break
    total = sum(sum_list)
    print(total)
    return total

x = [1, 2, 3]
list_sum_no_thirteen(x)

x = [5, 13, 77]
list_sum_no_thirteen(x)

x = [13, 22, 5]
list_sum_no_thirteen(x)
