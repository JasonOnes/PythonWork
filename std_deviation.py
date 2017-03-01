""" excercise in determining standard deviation"""


grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_nums(x):
    for num in x:
        print(num)

def num_sum(x):
    total = 0
    for num in x:
        total += num
    return total

def num_average(x):
    sumthing = num_sum(x)
    average = sumthing / float(len(x))
    return average

def num_variance(y):
    average = num_average(y)
    variance = 0
    for num in y:
        variance += (average - num) ** 2
    v = variance / len(y)
    return v

def num_std_deviation(v):
    return (num_variance(grades) ** 0.5)

#variance = num_variance(grades)
#print(num_std_deviation(variance))


print(grades)
print(num_sum(grades))
print(num_average(grades))
print(num_variance(grades))
print(num_std_deviation(v))
