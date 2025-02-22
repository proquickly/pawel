def multiply(queue, current, visited, cost, B):
    for X in range(2, B // current + 1):
        new_value = current * X
        if new_value == B:
            return cost + X, new_value
        if new_value < B and new_value not in visited:
            visited.add(new_value)
            queue.append((new_value, cost + X))
    return None, None  # Only after exhausting loop


def divide(queue, current, visited, cost, B):
    for Y in range(2, current + 1):
        if current % Y == 0:
            new_value = current // Y
            if new_value == B:
                return cost + Y, new_value
            if new_value > 0 and new_value not in visited:
                visited.add(new_value)
                queue.append((new_value, cost + Y))
    return None, None  # Only after exhausting loop


def min_bajtalars(A, B):
    if A == B:
        return 0

    queue = [(A, 0)]
    visited = {A}

    while queue:
        current, cost = queue.pop(0)  # O(n) operation

        cost1, new_value1 = multiply(queue, current, visited, cost, B)
        if new_value1 == B:
            return cost1

        cost2, new_value2 = divide(queue, current, visited, cost, B)
        if new_value2 == B:
            return cost2

    return -1


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(min_bajtalars(A, B))
