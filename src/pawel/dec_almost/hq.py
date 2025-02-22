from heapq import heappush, heappop

def min_cost_transform(A, B):
    if A == B:
        return 0

    # Priority queue to store (cost, current_number)
    queue = [(0, A)]
    # Dictionary to track visited numbers and their minimum costs
    visited = {A: 0}

    while queue:
        cost, current = heappop(queue)

        if current == B:
            return cost

        # Generate all possible transitions
        # 1. Multiply by x (where current * x <= 2*B)  # Changed this bound
        for x in range(2, (2 * B) // current + 1):  # Allow larger intermediate values
            new_num = current * x
            new_cost = cost + x

            if new_num > 2 * B:  # Allow going higher than B temporarily
                break
            if new_num in visited and visited[new_num] <= new_cost:
                continue

            visited[new_num] = new_cost
            heappush(queue, (new_cost, new_num))

        # 2. Divide by valid factors of current
        for y in range(2, int(current ** 0.5) + 1):
            if current % y == 0:
                # Try smaller divisor
                new_num = current // y
                new_cost = cost + y
                if new_num >= 1 and (new_num not in visited or visited[new_num] > new_cost):
                    visited[new_num] = new_cost
                    heappush(queue, (new_cost, new_num))

                # Try larger divisor
                larger_y = current // y
                if larger_y != y:
                    new_num = current // larger_y
                    new_cost = cost + larger_y
                    if new_num >= 1 and (new_num not in visited or visited[new_num] > new_cost):
                        visited[new_num] = new_cost
                        heappush(queue, (new_cost, new_num))

    return -1


# Test cases
print(min_cost_transform(1, 20))
print(min_cost_transform(1, 2))
print(min_cost_transform(1, 3))
print(min_cost_transform(3, 4)) # fails when divide AND multiply?
print(min_cost_transform(20, 22))

"""
multipy and divide are interacting with each other when both are needed"""


"""
The correct minimum cost to transform `3` into `4` is:
`5`.
This corresponds to the path:
- Multiply `3` by `2` to get `6` (cost `2`),
- Divide `6` by `3` to get `4` (cost `3`).
"""
