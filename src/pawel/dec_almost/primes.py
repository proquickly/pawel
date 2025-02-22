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


numbers = (741787296401, 13, 19, 9, 100, 49, 101)
for number in numbers:
    print(f"Prime factors of {number}: {find_prime_factors(number)}")
