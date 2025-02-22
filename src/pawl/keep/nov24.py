def min_bajtalars(A, B):
    if A == B:
        return 0

    queue = [(A, 0)]
    visited = {A}

    while queue:  # BFS
        current, cost = queue.pop(0)

        for X in range(2, B // current + 1):  # multiply
            new_value = current * X
            if new_value == B:
                return cost + X
            if new_value < B and new_value not in visited:
                visited.add(new_value)
                queue.append((new_value, cost + X))

        for Y in range(2, current + 1):  # divide
            if current % Y == 0:
                new_value = current // Y
                if new_value == B:
                    return cost + Y
                if new_value > 0 and new_value not in visited:
                    visited.add(new_value)
                    queue.append((new_value, cost + Y))

    return -1


# Reading the input
A, B = map(int, input().split())

# Print the minimum amount Bajtek has to pay
print(min_bajtalars(A, B))
