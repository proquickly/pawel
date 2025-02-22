def calculate_rectangle_dimensions(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))

    best_dimensions = min(factors, key=lambda x: abs(x[0] - x[1]))
    return best_dimensions[0], best_dimensions[1]


print(calculate_rectangle_dimensions(6))
