import math

def znajdz_najwiekszy_telewizor(H, W, diagonale):
    # Proportions 16:9
    ratio_width = 16
    ratio_height = 9
    diagonal_ratio = math.sqrt(ratio_width**2 + ratio_height**2)

    max_diagonal = -1  # First we set it to -1 which means theres no fit

    # We go through every diagonal
    for d in diagonale:
        # We calculate width and height in inches
        w_inch = (ratio_width / diagonal_ratio) * d
        h_inch = (ratio_height / diagonal_ratio) * d

        # Converting to centimiters
        w_cm = w_inch * 2.54
        h_cm = h_inch * 2.54

        # Check if the tv fits
        if w_cm <= W and h_cm <= H:
            max_diagonal = max(max_diagonal, d)

    # If max_diagonal is still -1 it means that no tv fitted
    if max_diagonal == -1:
        return "NIE"
    else:
        return str(max_diagonal)



if __name__ == "__main__":
    test_cases = [
        {"max_height": 100, "max_width": 150, "diagonals": [42,50,55]},#expect 55
        {"max_height": 170, "max_width": 150, "diagonals": [43,77,55,65,83]},#expect 65
        {"max_height": 100, "max_width": 100, "diagonals": [73,46,55,64]},#expect NIE
        {"max_height": 89, "max_width": 156, "diagonals": [70]},#expect 70
        {"max_height": 120, "max_width": 200, "diagonals": [60,75,85,90]},#expect 90
        {"max_height": 100, "max_width": 180, "diagonals": [55,65,75,85,95]},#expect 75
        {"max_height": 70, "max_width": 100, "diagonals": [32,40,48,55]},#expect 40
        {"max_height": 95, "max_width": 160, "diagonals": [55,60,65,70]},#expect 70
        {"max_height": 85, "max_width": 140, "diagonals": [43,50,55,65]},#expect 55
        {"max_height": 65, "max_width": 110, "diagonals": [42,46,50,58]},#expect 46
        {"max_height": 100, "max_width": 130, "diagonals": [49,55,60,65]},#expect 55
    ]

    results = []

    for case in test_cases:
        max_height = case["max_height"]
        max_width = case["max_width"]
        diagonals = case["diagonals"]

        result = znajdz_najwiekszy_telewizor(max_height, max_width, diagonals)
        results.append(result)

    for res in results:
        print(res)


"""
height width: 50 90
number variants: 5
diagonals: 20 25 30 35 40
expected 25

height width: 100 100
number variants: 3
diagonals: 50 48 46
expected 48

height width: 60 80
number variants: 2
diagonals: 35 45
expected NO

        {"max_height": 170, "max_width": 150, "diagonals": [43,77,55,65,83]},
        {"max_height": 100, "max_width": 100, "diagonals": [73,46,55,64]},
        {"max_height": 89, "max_width": 156, "diagonals": [70]},
"""