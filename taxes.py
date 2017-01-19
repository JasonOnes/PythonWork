def oregon_income_tax():
    x = int(input("Your income here:  "))
    total = list()

    if x > 116000:
        y = (x - 116000) * 0.099
        total.append(y)
        if x < 116000 and x > 8400:
            #y = 3350 * 0.05
            total.append((x - 8400) * 0.09)
            print(total)
            if x < 8400 and x > 3350:
                total.append((x-3350) * 0.07)
                print(total)
                if x <= 3350:
                    total.append(x * 0.05)
                    print(total)
                #if x > 124400:
        #total.apppen((x-124400) * 0.099)
        #print(total)"""
    print(sum(total))

oregon_income_tax()
