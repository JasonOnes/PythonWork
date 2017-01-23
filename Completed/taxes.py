
def taxes():
    x = int(input("How much did you make last year? "))
    total = list()
    if x >= 3350:
        total.append(3350 * 0.05)
        x -= 3350
    else:
        total.append(x * 0.05)
        x = 0
    if x >= 5050:
        y = 5050 * 0.07
        total.append(y)
        x -= 5050
    else:
        total.append(x * 0.07)
        x = 0
    if x >= 116000:
        total.append(116000 * 0.09)
        x -= 116000
        total.append(x * 0.099)
    else:
        total.append(x * 0.09)
        x = 0

    print(sum(total))

taxes()
