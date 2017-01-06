""" Counting change using the smallest number of coins.
    Give the amount of money left in the till after the
    transaction.
    """


def count(m, x):

    double_saws = 2000
    saw_bucks = 1000
    fins = 500
    bill = 100
    quarter = 25
    dime = 10
    nickle = 5
    penny = 1

    cents = x
    money_in_till = m

    twens = cents // double_saws
    money_in_till = m - twens
    cents = cents - (twens * double_saws)

    tens = cents // saw_bucks
    money_in_till = money_in_till - tens
    cents = cents - (tens * saw_bucks)

    fvs = cents // fins
    money_in_till = money_in_till - fvs
    cents = cents - (fvs * fins)

    bls = cents // bill
    money_in_till = money_in_till - bls
    cents = cents - (bls * bill)

    qs = cents // quarter
    money_in_till = money_in_till - qs
    cents = cents - (qs * quarter)

    dms =  cents // dime
    money_in_till = money_in_till - dms
    cents = cents - (dms * dime)

    ncks = cents // nickle
    money_in_till = money_in_till - ncks
    cents = cents - (ncks * nickle)

    pns = cents // penny
    money_in_till = money_in_till - pns

    money_in_till = money_in_till
    twens_left = money_in_till // double_saws
    money_in_till = money_in_till - (twens_left * double_saws)
    print(money_in_till)

    tens_left = money_in_till // saw_bucks
    money_in_till = money_in_till - (tens_left * saw_bucks)
    print(money_in_till)

    fives_left = money_in_till // fins
    money_in_till = money_in_till - (fives_left * fins)
    print(money_in_till)

    bls_left = money_in_till // bill
    money_in_till = money_in_till - (bls_left * bill)
    print(money_in_till)

    qtrs_left = money_in_till // quarter
    money_in_till = money_in_till - (qtrs_left * quarter)
    print(money_in_till)

    dms_left = money_in_till // dime
    money_in_till = money_in_till - (dms_left * dime)
    print(money_in_till)

    ncks_left = money_in_till // nickle
    money_in_till = money_in_till - (ncks_left * nickle)
    print(money_in_till)

    pens_left = money_in_till // penny
    money_in_till = money_in_till - (pens_left * penny)


    print(money_in_till)

    print("{} double saw bucks, \n{} saw bucks, \n{} fins, \n{} bills, \n{} quarters, \
     \n{} dimes,\n{} nickles, \n{} pennies".format(twens, tens, fvs, bls, qs,
                                                    dms, ncks, pns))
    print("*" * 100)
    print("{} left in till!".format(money_in_till))
    print("{} double saw bucks, \n{} saw bucks, \n{}fins, \n{} bills, \n{} quarters, \
    \n{} dimes, \n{} nickles, \n{} pennies".format(twens_left, tens_left, fives_left,
                                                   bls_left, qtrs_left, dms_left,
                                                   ncks_left, pens_left))

count(43000, 12489)
