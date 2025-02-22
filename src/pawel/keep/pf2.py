def generate_minimal_figure(N):
    if N == 1:
        return "URDL"  # A single cell can be represented by a closed loop

    side_len = 1
    while side_len * side_len < N:
        side_len += 1

    figure = []

    if side_len * (side_len - 1) >= N:
        shorter_side = side_len - 1
        cells_to_fill = N
        for row in range(shorter_side):
            if row % 2 == 0:
                figure.append('R' * (side_len - 1))
                figure.append('U')
            else:
                figure.append('L' * (side_len - 1))
                figure.append('U')

            cells_to_fill -= side_len - 1

            if cells_to_fill <= 0:
                break

        if cells_to_fill > 0:
            last_row_fill = 'R' * (cells_to_fill // 2)
            if cells_to_fill % 2 == 1:
                last_row_fill += 'R'
            figure.append(last_row_fill)
        figure.append('D' * (
            shorter_side if shorter_side % 2 == 0 else shorter_side - 1))
        figure.append(
            'L' * (side_len - 1 if side_len % 2 != 0 else side_len - 2))
    else:
        cells_to_fill = N
        for row in range(side_len):
            if row % 2 == 0:
                figure.append('R' * (side_len - 1))
                figure.append('U')
            else:
                figure.append('L' * (side_len - 1))
                figure.append('U')

            cells_to_fill -= side_len - 1

            if cells_to_fill <= 0:
                break

        if cells_to_fill > 0:
            last_row_fill = 'R' * (cells_to_fill // 2)
            if cells_to_fill % 2 == 1:
                last_row_fill += 'R'
            figure.append(last_row_fill)
        figure.append('D' * (side_len - 1))
        figure.append('L' * (side_len - 1))

    return ''.join(figure)


# Read input
N = int(input().strip())

# Generate figure description
result = generate_minimal_figure(N)

# Print result
print(result)
