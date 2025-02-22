import math
#import pysnooper
"""Bytesia got a beautiful new squared notebook. Now her job is to draw a figure limited to
notebook pages. He draws each figure with his pencil. Starting from a certain corner of the grid, 
then without lifting the pencil
draws a border around the edges of the grids if it does not return to the starting point. 
Bytesia makes sure that the pencil doesn't go through
undesirable point, other than the starting point, more than once. The drawn line does not intersect.
An example of a figure that can be used to draw Byte.
The drawing drawn by Byte is easy using strings of characters denoting subsequent pencil actions. The letter G
means moving the pencil up one square. Similarly, the letters D, L and P mean movement down, left and right.
For example, the description of the figure being snapped higher 
(if Byte was drawn in the lower left corner, drawing upwards) to
GGPPPGLGPPPDDPPDDLLLLGLDL.
Her younger brother, admiring her work, requested Bytesia to get to the initial custom figure.
He would want this figure to have exactly 𝑁 squares inside. Bytesia, of course, will not refuse her brother, 
but she already has plans
Further ideas, so remove this figure like a cable. Help her and write the shortest description of the figure she has
inside exactly 𝑁 squares."""
# import pysnooper

# print(draw(2, 4, 0))
# print(get_more_squareish(inp))
# print(solve(inp))

"""
SCENARIOS
1.if the ratio is good and the number is even we are done

2.if the ratio is not good and the number is even we have to adjust:
  - we need to find the nearest rectangle/square with a good ratio by 
  iterating substracting 1 from the area and adding 1 to the extra blocks 
  until the ratio is good
  - we need to calculate either the extra or the unneeded squares to acheive n,
    then

PROBLEM
when i send the code that is "correct" it says on the input "12456789" the output could be shorter but is still correct(so we got 76 points).
I cant imagine what could be the correct width, height and extra blocks for 123456789.
if i had to guess i think the problem is that shape with the smallest area is not square/rectangle but circle OR
the problem is in the "get best dimensions" function
i think the function could maybe sacrifice some width and height to get more squareish and add extra blocks

input: 123456789
output: (the lenght of the "G","L" ect. is 141714) WIDTH:10821 HEIGHT:11409 EXTRA BLOCKS:0
assumption: could somehow add extra blocks for smaller lenght of the directions(G,L,D,G)

"""

def check_is_even(n):
    return n % 2 == 0


def check_is_odd(n):
    return n % 2 != 0


def check_is_ratio_good(width, height):
    ratio = max(width, height) / min(width, height)
    return ratio <= 2


def get_best_dimensions(n):
    root = int(math.sqrt(n))
    for i in range(root, 0, -1):
        if n % i == 0:
            return i, n // i
    return 1, n

def draw_for_prime(width,height,extra_blocks):
    string = ""

    for g in range(height):
        string += "G"
    for p in range(width):
        string += "P"
    if extra_blocks > 0:
        string += "P"
    for d in range(extra_blocks):
        string += "D"
    if extra_blocks > 0:
        string += "L"
    for d in range(height - extra_blocks):
        string += "D"
    for l in range(width):
        string += "L"

    return string

def draw_for_non_prime(width,height,extra_blocks):#3,3,7
    string = ""

    down = height + extra_blocks # 10
    up = height # 3
    difference = down - up # 7
    extra_rows = extra_blocks // height # 7 // 3 = 2
    extra_rows_remainder = extra_blocks % height# 7 mod 3 = 1
    
    if difference > 0:
        for _ in range(height): string += "G"
        for _ in range(width+extra_rows): string += "P" # WIDTH + 1
        #if extra_rows_remainder > 0:
        #    for _ in range(1): string += "P" #IF NO REMAINDER THEN ITS NOT NEEDED
        #    for _ in range(extra_rows_remainder): string += "D"
        #    for _ in range(height): string += "L"
        for _ in range(height): string += "D"
        if extra_rows_remainder > 0:
            for _ in range(1): string += "D" #IF NO REMAINDER THEN ITS NOT NEEDED
            for _ in range(extra_rows_remainder): string += "L"
            for _ in range(1): string += "G"
            for _ in range(width - extra_rows_remainder): string += "L"
        else:
            for _ in range(extra_rows): string += "L"
            for _ in range(width): string += "L"
        return string
        """
        if the difference between the up and down is positive
        THEN WE NEED TO SUBSTRACT FROM THE DOWN LINE UNTIL THE
        BASE LINE IS ON THE SAME LEVEL AS THE LEFT LINE
        """

    else:
        for g in range(height):
            string += "G"
        for p in range(width):
            string += "P"
        if extra_blocks > 0:
            string += "P"
        for d in range(extra_blocks):
            string += "D"
        if extra_blocks > 0:
            string += "L"
        for d in range(height - extra_blocks):
            string += "D"
        for l in range(width):
            string += "L"
        return string


def prime(n):
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

def get_more_squareish(n):
    is_even = check_is_even(n)
    is_odd = check_is_odd(n)
    extra_blocks = 0


    if prime(n):
        is_prime = True
        if is_even:
            width, height = get_best_dimensions(n)
            while not check_is_ratio_good(width, height):
                n -= 1
                extra_blocks += 1
                width, height = get_best_dimensions(n)
        elif is_odd:
            width, height = get_best_dimensions(n)
            while not check_is_ratio_good(width, height):
                n -= 1
                extra_blocks += 1
                width, height = get_best_dimensions(n)
        
        return width, height, extra_blocks, is_prime
    
    else:
        is_prime = False
        square_root_of_n = n ** 0.5
        square = int(square_root_of_n) ** 2
        extra_blocks = n - square

        width, height = int(square_root_of_n), int(square_root_of_n)
        #print(f"{width=},{height=},{extra_blocks=}")
        #input()

        return width, height, extra_blocks, is_prime
#@pysnooper.snoop(depth=2)
def draw(width, height, extra_blocks, is_prime):
    if is_prime:
        string = draw_for_prime(width,height,extra_blocks)
    else:
        string = draw_for_non_prime(width, height, extra_blocks)
    return string




def solve(n):
    width, height, extra_blocks, is_prime = get_more_squareish(n)
    return draw(width, height, extra_blocks, is_prime)


inp = int(input())
print(solve(inp))

#inputs = [2,3,4,5,8,9,13,100,103,2319078]
#for i in inputs:
#    print(f"Input: {i}")
#    print(solve(i))
#    print()