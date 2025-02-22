import pysnooper

@pysnooper.snoop()
def multiply(queue, current, visited, cost, B):
    for X in range(2, B // current + 1):
        new_value = current * X
        while True:
            # what?
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

# How to fix the program:

# 1. Do small steps for multiplying:
#    - Instead of doing 1 * 20 right away break it into smaller steps like
#      1 * 2 * 2 * 5. This way it can find the best way to get to B.

# 2. Always check the smallest cost first:
#    - Keep the numbers you want to try in a list or queue and always
#      work on the number with the smallest cost first. This helps
#      find the easiest way.

# 3. For dividing start with small numbers:
#    - Divide by small numbers like 2 or 3 firsT not big ones. This
#      makes it more likely to find the best path.

# 4. Dont do the same thing twice:
#    - If you’ve already tried a number and it cost less before, skip it.
#    - Keep track of numbers you’ve already checked with their costs.

# 5. Dont stop too soon:
#    - Even if you find B, dont stop right away. Keep looking to make sure
#      there isnt a cheaper way to get to B.

# What the program should do:
# - Start with A and a cost of 0.
# - For every number in the list:
#     * Try multiplying by small numbers one by one.
#     * Try dividing by small numbers one by one.
#     * Add the new numbers to the list with their costs.
# - Always work on the number with the smallest cost first.
# - When you reach B for the first time, it will be the cheapest way.

# How the function would work step-by-step:

# 1. Start with A
#    - Put A in a queue with a starting cost of 0
#    - Also keep a "visited" set or dictionary to remember which numbers
#      you’ve already checked and their lowest cost

# 2. Use a loop to keep processing numbers in the queue
#    - Take the first number (current number) and its cost from the queue
#    - Check if the current number is B
#        * If yes return the cost because this is the cheapest way to get to B

# 3. Multiply step
#    - Try multiplying the current number by 2 3 4 and so on
#    - For each new number
#        * If the new number is less than or equal to B and not already visited
#            - Add it to the queue with its new cost
#            - Mark it as visited

# 4. Divide step
#    - Try dividing the current number by 2 3 4 and so on
#    - For each new number
#        * If the result is greater than 0 and not already visited
#            - Add it to the queue with its new cost
#            - Mark it as visited

# 5. Keep going
#    - The loop continues always working on the number with the smallest cost first
#      (this happens naturally if you use a priority queue or process the queue in order)
#    - When you find B return its cost

# 6. If the queue becomes empty
#    - If you finish the loop and never reach B return -1 This means it’s not
#      possible to transform A into B
