"""
Note: this task is an open task. You can check the result of your submission
in the SIO2 system.
Byteasar works as a programmer in a glass office building of a Bytite
corporation. After a hard day of mental work, he usually
just wants to relax in front of the TV. His old TV is barely coping,
probably only displaying
advertisement blocks well. Byteasar's attention was caught by the offer of a
modern TV tailored to his needs. In addition, it can be
purchased in zero percent installments, so the price is not a factor.
Byteasar hopes that by the time he has to pay the first
installment, he will have managed to get a promotion and the desired raise.

The TV in the ad is ultra-thin and frameless, its thickness is practically
zero, it has a rectangular shape, and its entire surface is occupied by the
screen. There are models of this TV with different screen diagonals, usually
given in inches, but all
models have a standard, typical ratio of width to height of the screen,
which is 16:9.
Byteasar would of course like to buy himself the largest possible TV,
but there is a problem: the TV must fit on
the dresser above the fireplace, and it cannot be turned, so its height
cannot exceed 𝐻 centimeters, and its width
cannot exceed 𝑊 centimeters. What kind of TV should Byteasar buy? Help him
and write a program that
will select from the models available in the store the largest possible TV
that will fit on the dresser.

Assume that one inch is exactly 2.54 centimeters.

Input
The first line of input contains two natural numbers 𝐻 and 𝑊 (1 ≤ 𝐻,
𝑊 ≤ 250), separated by a single
space. They define the maximum height and maximum width of the TV screen in
centimeters.

The second line of input contains one natural number 𝑁 (1 ≤ 𝑁 ≤ 10)
defining the number of available TV variants.

The third (last) line of input contains a sequence of 𝑁 natural numbers
𝐴𝑖 (1 ≤ 𝐴𝑖 ≤ 120) separated by single
spaces. These are the lengths of the screen diagonals (in inches) of the
available TV models.

Output
In the first (only) line of output, you should write out the largest (among
those given in the input) TV diagonal
that Byteasar can buy for his home.

If none of the available TV models will fit on the dresser, you should write
out one word NO.

You can solve the task in several simpler variants. Some test groups meet
certain additional restrictions.
The table below shows how many points your program would receive if it
passed the tests with this restriction.

Explanation of the example: A 65-inch diagonal TV screen with a 16:9 aspect
ratio is approximately 31.87 inches (approx. 80.95 cm) high,
and approximately 56.65 inches (approx. 143.89 cm) wide. This is the largest
TV available that fits within the given
dimensions of 170 cm × 150 cm.
"""
h, w = input("height width: ").split(" ")
h, w = int(h), int(w)
n = input("number variants: ")
n = int(n)
diagonals = input("diagonals: ").split(" ")
diagonals = [int(diagonal) for diagonal in diagonals]

def main():
    def fits_on_dresser(diagonal):
        diagonal_cm = diagonal * 2.54
        aspect_ratio = 16 / 9
        width = ((diagonal_cm ** 2) / (aspect_ratio ** 2 + 1)) ** 0.5
        height = aspect_ratio * h
        return height <= h and width <= w

    largest_diagonal = 0
    for diagonal in diagonals:
        if fits_on_dresser(diagonal):
            largest_diagonal = max(largest_diagonal, diagonal)

    if largest_diagonal > 0:
        print(largest_diagonal)
    else:
        print("NO")


if __name__ == "__main__":
    main()

"""
height width: 170 150
number variants: 5
diagonals: 65 60 55 50 45
expected 65

height width: 50 90
number variants: 5
diagonals: 20 25 30 35 40
expected 25

height width: 100 100
number variants: 3
diagonals: 50 48 46
expected 48

height width: 120 200
number variants: 3
diagonals: 100 120 75
expcted 75

height width: 60 80
number variants: 2
diagonals: 35 45
expected NO

"""
