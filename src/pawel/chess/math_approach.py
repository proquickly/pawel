import math

def mathh(n):
    # Funkcja zwraca resztę z dzielenia n przez 4
    n2 = n / 4
    n2 = math.floor(n2)
    return n - (n2 * 4)

def draw(n):
    if n == 1:
        return "GPDL"
    elif n == 2:
        return "GGPDDL"
    elif n == 3:
        return "GPDPDLLG"
    elif n == 4:
        return "GGPPDDLL"
    else:
        wall = n - mathh(n)
        extra = mathh(n)

        if wall == 0:
            return ""  # lub zwróć cokolwiek innego sensownego

        # Szukamy par dzielników
        factors = []
        for i in range(1, int(wall ** 0.5) + 1):
            if wall % i == 0:
                factors.append((i, wall // i))


        if not factors:
            return ""

        # Wybieramy parę dzielników, dla której różnica jest najmniejsza
        best_dimensions = min(factors, key=lambda x: abs(x[0] - x[1]))
        width, height = best_dimensions

        string = ""

        # Doklejamy kolejne segmenty łańcucha zgodnie z założeniem
        for g in range(height):
            string += "G"
        for p in range(width):
            string += "P"
        string += "P"

        for d in range(extra):
            string += "D"

        string += "L"

        for d in range(height - extra):
            string += "D"
        for l in range(width):
            string += "L"

        return string

inp = int(input())
result = draw(inp)
print(result)
