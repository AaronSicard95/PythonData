def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    for i in range(1,int(num/2)):
        print(num%i)
        if num%i == 0:
            if not i in factors:
                factors.append(i)
            if not i/num in factors:
                factors.append(int(num/i))
    return factors