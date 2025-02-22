from heapq import heappush, heappop
import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
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

    queue = [(0, A)]  # Stores tuples of (cost, current value)
    visited = {A: 0}  # Key: number, Value: minimum cost to reach it

    while queue:
        cost, current = heappop(queue)

        # If we reached the target, return the cost
        if current == B:
            return cost

        # Avoid redundant exploration
        if visited[current] < cost:
            continue

        # Multiplication transitions
        limit = (
                            2 * B) // current + 1  # Avoid multiplying beyond practical usefulness
        for x in range(2, limit):
            new_num = current * x
            new_cost = cost + x

            # Break early if value exceeds bounds
            if new_num > 2 * B:
                break

            # Update states if it's a better cost
            if new_num not in visited or visited[new_num] > new_cost:
                visited[new_num] = new_cost
                heappush(queue, (new_cost, new_num))

        # Division transitions by valid factors
        for y in range(2, int(current ** 0.5) + 1):
            if current % y == 0:
                # Divide by smaller factor
                smaller_factor = current // y
                new_cost = cost + y
                if smaller_factor >= 1 and (
                        smaller_factor not in visited or visited[
                    smaller_factor] > new_cost):
                    visited[smaller_factor] = new_cost
                    heappush(queue, (new_cost, smaller_factor))

                # Divide by larger corresponding factor
                larger_factor = y
                new_cost = cost + larger_factor
                if larger_factor >= 1 and (
                        larger_factor not in visited or visited[
                    larger_factor] > new_cost):
                    visited[larger_factor] = new_cost
                    heappush(queue, (new_cost, current // larger_factor))

    return -1


# Test cases
print(min_cost_transform(1, 20))
print(min_cost_transform(1, 2))
print(min_cost_transform(1, 3))
print(min_cost_transform(3, 4))
print(min_cost_transform(20, 22))
print(min_cost_transform(1, 7000000))
