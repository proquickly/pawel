from heapq import heappush, heappop
import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # also time.process_time()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Ran {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def min_cost_transform(A, B):
    if A == B:
        return 0

    queue = [(0, A)]
    visited = {A: 0}

    while queue:
        cost, current = heappop(queue)

        if current == B:
            return cost

        # Generate all possible transitions
        for x in range(2, (2 * B) // current + 1):
            # intermediate values
            new_num = current * x
            new_cost = cost + x

            if new_num > 2 * B:
                break
            if new_num in visited and visited[new_num] <= new_cost:
                continue

            visited[new_num] = new_cost
            heappush(queue, (new_cost, new_num))

        # 2. Divide by valid factors of current
        for y in range(2, int(current ** 0.5) + 1):
            if current % y == 0:
                new_num = current // y
                new_cost = cost + y
                if new_num >= 1 and (
                        new_num not in visited or visited[new_num] > new_cost):
                    visited[new_num] = new_cost
                    heappush(queue, (new_cost, new_num))

                larger_y = current // y
                if larger_y != y:
                    new_num = current // larger_y
                    new_cost = cost + larger_y
                    if new_num >= 1 and (new_num not in visited or visited[
                        new_num] > new_cost):
                        visited[new_num] = new_cost
                        heappush(queue, (new_cost, new_num))

    return -1


# Test cases
print(min_cost_transform(1, 20))
print(min_cost_transform(1, 2))
print(min_cost_transform(1, 3))
print(min_cost_transform(3, 4))
print(min_cost_transform(20, 22))
print(min_cost_transform(1, 741787296401))

"""
multipy and divide are interacting with each other when both are needed"""

"""
The correct minimum cost to transform `3` into `4` is:
`5`.
This corresponds to the path:
- Multiply `3` by `2` to get `6` (cost `2`),
- Divide `6` by `3` to get `4` (cost `3`).
"""
