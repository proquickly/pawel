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


def find_min_cost(A, B):
    if A == B:
        return 0

    a_factors = find_prime_factors(A)
    b_factors = find_prime_factors(B)

    a_count = {}
    b_count = {}

    for factor in a_factors:
        a_count[factor] = a_count.get(factor, 0) + 1
    for factor in b_factors:
        b_count[factor] = b_count.get(factor, 0) + 1

    total_cost = 0
    all_factors = set(a_count.keys()) | set(b_count.keys())

    for factor in all_factors:
        count_in_a = a_count.get(factor, 0)
        count_in_b = b_count.get(factor, 0)

        if count_in_b > count_in_a:
            total_cost += factor * (count_in_b - count_in_a)
        elif count_in_a > count_in_b:
            total_cost += factor * (count_in_a - count_in_b)

    return total_cost


def solve(A, B):
    result = find_min_cost(A, B)
    print(result)


A, B = map(int, input().split())
solve(A, B)
