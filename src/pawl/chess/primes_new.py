"""
Bajtek has a natural number A, but he would like to have a natural number B.
To achieve this, he can go to Bajtosia, who, for a fee of X bajtalars,
can multiply his number by X. He can also go to Bajtyna, who, for a fee of Y
bajtalars, can divide his number by Y, but only if Bajtek's number is
divisible by Y.

Please note that Bajtek decides whether and how many times he wants to use
the girls' services, and he also chooses the values of the parameters X and
Y. The only constraint is that X and Y must be natural numbers because there
are no denominations smaller than one bajtalar.

Bajtek is frugal and wants to spend as few bajtalars as possible. Help him
determine the minimum amount he must pay the girls to achieve his goal of
transforming the number A into the number B.

Input

The first (and only) line of the input contains two natural numbers A and B
(1 ≤ A, B ≤ 10¹²) separated by a single space. They represent, respectively,
the number that Bajtek currently has and the number he wants to obtain.

Output

Find the minimum cost for Bajtek to transform the number ( A ) into ( B ) 
using the following operations:
1. Multiplying his number by ( X ) at a cost of ( X ) bajtalars.
2. Dividing his number by ( Y ) at a cost of ( Y ) bajtalars, but only if
his number is divisible by ( Y ).
"""

import pysnooper


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def find_prime_factors(n):
    if is_prime(n):
        return [n]
    prime_factors = []

    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            prime_factors.append(factor)
            n //= factor
        factor += 2

    if n > 2:
        prime_factors.append(n)

    return prime_factors


def minimal_cost(factors: list, A, B):
    if A == B:  # CORRECT
        cost = 0
        return cost

    elif A == 1:  # CORRECT
        cost = 0
        for factor in factors:
            A *= factor
            if A > B:
                break
            cost = cost + factor
            A *= factor
            cost += factor
            B //= factor
    elif B == 1:  # CORRECT
        cost = 0
        for factor in factors:
            B //= factor
            cost = cost + factor
        return cost

    elif A > B:  # SUSPICIOUS
        cost = 0
        while A > B:
            for factor in factors:
                if A % factor == 0:
                    A //= factor
                    cost += factor
                    break
            else:
                break
        return cost + (A - B) if A >= B else float('inf')
    elif A < B:  # SUSPICIOUS
        cost = 0
        while A < B:
            for factor in factors:
                A *= factor
                cost += factor
                if A >= B:
                    break
        return cost + (A - B) if A >= B else float('inf')


# @pysnooper.snoop()
def solve(A, B):
    a_factors = find_prime_factors(A)
    b_factors = find_prime_factors(B)
    a_cost = minimal_cost(a_factors, A, B)
    if A < B:
        a_cost = minimal_cost(b_factors, A, B)
        print(f"{a_cost}")
    else:
        b_cost = minimal_cost(b_factors, A, B)
        print(f"{b_cost}")


# print(f"Prime factors of {number}: {find_prime_factors(number)}")
# print(minimal_cost(find_prime_factors(number), 1, number))
# solve(1,20) WORKS
# solve(20,1)
A, B = map(int, input().split())
solve(A, B)
