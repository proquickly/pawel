"""
Bajtek has a natural number A, but he would like to have a natural number B.
To achieve this, he can go to Bajtosia, who, for a fee of X bajtalars,
can multiply his number by X. He can also go to Bajtyna, who, for a fee of Y
bajtalars, can divide his number by Y, but only if Bajtek's number is
divisible by Y.

Please note that Bajtek decides whether and how many times he wants to use
the girls' services, and he also chooses the values of the parameters X and
Y. The only constraint is that X and Y must be natural numbers because there
are no denominations smaller than one bajtalar.

Bajtek is frugal and wants to spend as few bajtalars as possible. Help him
determine the minimum amount he must pay the girls to achieve his goal of
transforming the number A into the number B.

Input

The first (and only) line of the input contains two natural numbers A and B
(1 ≤ A, B ≤ 10¹²) separated by a single space. They represent, respectively,
the number that Bajtek currently has and the number he wants to obtain.

Output

Find the minimum cost for Bajtek to transform the number ( A ) into ( B ) 
using the following operations:
1. Multiplying his number by ( X ) at a cost of ( X ) bajtalars.
2. Dividing his number by ( Y ) at a cost of ( Y ) bajtalars, but only if
his number is divisible by ( Y ).

Breadth-First Search (BFS) can find the shortest path from the number ( A )
to the number ( B ) in the graph of possible transformations. The cost of 
the shortest path (in terms of transformation cost) from the number ( A ) to the number ( B ) is found.

### Example: ( A = 2 ) and ( B = 10 )
1. **Initial Node**: ( (2, 0) ) where 2 is the current number and 0 is the 
initial cost.
2. **Possible Transformations**:
    - Multiplying by ( X ) (where ( X ) ranges from 2 to ( B // \text{current number} )).
    - Dividing by ( Y ) (where ( Y ) is any divisor of the current number).

Here’s how BFS would explore the graph step-by-step.
### Graph Construction:
1. **Level 0** (Start at 2):
    - Node: ((2, 0))

2. **Level 1** (Multiply by 2 through 10 // 2):
    - Multiply by 2: ((4, 2))
    - Multiply by 3: ((6, 3))
    - Multiply by 4: ((8, 4))
    - Multiply by 5: ((10, 5)) ← Target reached

So, the graph would look something like this:

           2 (0)
       /  |    \     \
      /   |     \     \
 `(2+2) (2+3) (2+4) (2+5)
  4 (2) 6 (3) 8 (4) 10 (5)
    |
    | 
    ...

**Level 0**:
- Start from ((2, 0)).

**Level 1**:
- Expand ((2, 0)):
    1. Multiply by 2: ((4, 2)), enqueued if not visited.
    2. Multiply by 3: ((6, 3)), enqueued if not visited.
    3. Multiply by 4: ((8, 4)), enqueued if not visited.
    4. Multiply by 5: ((10, 5)), target reached, return cost 5.

"""
