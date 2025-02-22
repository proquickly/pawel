def is_power(num, n):
    if num == 1:
        return True
    base = 2
    while base ** n <= num:
        if base ** n == num:
            return True
        base += 1
    return False


print(is_power(64, 6))

"""Checks whether 8 can be expressed as an integer raised to the 
power of 3."""
