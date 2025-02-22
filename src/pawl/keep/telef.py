from typing import List, Dict

# Mapping of digits to letters
DIGIT_TO_LETTERS = {
    '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
    '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'
}


def count_encodings(digits: str) -> int:
    if not digits:
        return 1
    return len(DIGIT_TO_LETTERS[digits[0]]) * count_encodings(digits[1:])


def find_kth_encoding(digits: str, k: int) -> str:
    if not digits:
        return ""

    letter_count = count_encodings(digits[1:])
    current_digit = digits[0]
    letters = DIGIT_TO_LETTERS[current_digit]

    for i, letter in enumerate(letters):
        if k <= (i + 1) * letter_count:
            return letter + find_kth_encoding(digits[1:], k - i * letter_count)


def solve(phone_number: str, k: int) -> str:
    return find_kth_encoding(phone_number, k)


test_cases = [
    ("84", 7),
    ("645", 25),
    ("8378", 22),
    ("22586742", 3022),
    ("8353366", 458)
]

for phone_number, k in test_cases:
    result = solve(phone_number, k)
    print(f"Phone number: {phone_number}, K: {k}")
    print(f"Result: {result}")
    print()
