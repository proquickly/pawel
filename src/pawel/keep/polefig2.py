def calculate_area(description):
    x, y = 0, 0
    vertices = [(0, 0)]

    valid_moves = {'G', 'D', 'P', 'L'}

    for move in description:
        if move not in valid_moves:
            raise ValueError(f"Invalid move character: '{move}'")
        if move == 'G':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'P':
            x += 1
        elif move == 'L':
            x -= 1
        vertices.append((x, y))

    if vertices[-1] != vertices[0]:
        raise ValueError("The path does not form a closed polygon")

    n = len(vertices)
    area = 0
    for i in range(n - 1):
        area += vertices[i][0] * vertices[i + 1][1]
        area -= vertices[i + 1][0] * vertices[i][1]

    return abs(area) // 2


descriptions = [
    "GGPPPGLGPPDDPPDDLLLLGLDL",
    "GGPPDDLL",
    "LLGGGPDPGPDDDL",
    "GGPPPPPPDDLLLLLL"
]
for description in descriptions:
    try:
        result = calculate_area(description)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
