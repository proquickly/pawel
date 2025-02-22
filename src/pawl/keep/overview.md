overview of nov24.py:

The program defines a function min_bajtalars that attempts to compute the
minimum "cost" required to transform an integer A into another integer B using
two types of operations: multiplication and division by integers greater than
or equal to 2. The function uses a Breadth-First Search (BFS) approach to
explore all possible transformations.
Here's a breakdown of how the code works:

Base Case Check:

If A is already equal to B, it returns 0 immediately since no operations are
needed.
Initialization:

A queue is initialized with the tuple (A, 0) where A is the current value and 0
is the initial cost.
A set named visited is initialized to keep track of numbers that have already
been processed to avoid redundant operations.
Breadth-First Search (BFS) Loop:

The code uses a while loop to process each number in the queue.
For each number (current) in the queue, its cost is also stored.
Multiplication Operations:

The first for loop iterates over possible multipliers X starting from 2.
It calculates new_value as current * X.
If new_value equals B, it returns the cost + X as the total cost.
If new_value is less than B and hasn't been visited, it's added to the queue
with the updated cost and marked as visited.
Division Operations:

The second for loop iterates over possible divisors Y starting from 2.
It checks if current is divisible by Y and calculates new_value as current //
Y.
If new_value equals B, it returns the cost + Y as the total cost.
If new_value hasn't been visited and is greater than 0, it's added to the queue
with the updated cost and marked as visited.
Return Statement:

If all possibilities have been explored and it wasn't possible to transform A
into B, the function returns -1.
Input and Output:

The program reads two integers from the input, A and B.
It prints out the result of the min_bajtalars function, which is the minimum
cost Bajtek has to pay.
