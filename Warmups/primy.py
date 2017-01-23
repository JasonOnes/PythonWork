def max_primy(n):
    big_prime = 0
    for num in range(n):
        for i in range(2, n-1):
            if num % i == 0:
                break
            else:
                big_prime = num
    print(big_prime)
    return big_prime


max_primy(100)
