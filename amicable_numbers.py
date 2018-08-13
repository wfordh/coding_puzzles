import numpy as np

def get_proper_divisors(M):
    """
    Basic function to find the proper divisors for a specified function
    :M: integer
    """
    divisors = list()
    for i in np.arange(1, np.ceil(np.sqrt(M)).astype(int)):
        if M % i == 0:
            divisors.append(i)
            if i != 1:
                divisors.append(int(M/i))
    
    return divisors

def is_amicable_num(L, K):
    """
    Determine if two numbers are amicable. Amicable numbers are 
    such that the proper divisors of one add up to the other, as
    well as the other way around.
    :L: integer
    :K: integer
    """
    L_prop = get_proper_divisors(L)
    K_prop = get_proper_divisors(K)
    return (sum(L_prop) == K) & (sum(K_prop) == L)

def get_amicable_nums(N):
    """
    Find all amicable numbers up to an integer, non-inclusive.
    :N: integer
    """
    amicable_nums = set()
    for i in np.arange(1, N):
        prop_divs = get_proper_divisors(i)
        sum_prop_divs = np.sum(prop_divs)
        if is_amicable_num(i, sum_prop_divs) & (i != sum_prop_divs):
            amicable_nums.add(i)
            amicable_nums.add(sum_prop_divs)
    
    return amicable_nums