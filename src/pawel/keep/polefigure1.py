import math

def generate_figure_description(N):
    if N == 1:
        return "URDL"

    # Find the dimensions of the largest rectangle that fits
    width = int(math.sqrt(N))
    height = N // width
    remaining = N - (width * height)

    description = ""

    # Draw the main rectangle
    description += "R" * width + "U" * height + "L" * width + "D" * height

    # Handle remaining cells
    if remaining > 0:
        description = description[:-height]  # Remove last 'D' moves
        description += "R"  # Move right to start the extension

        full_columns = remaining // height
        partial_column = remaining % height

        # Add full columns
        for _ in range(full_columns):
            description += "U" * height + "R" + "D" * height + "R"

        # Add partial column if needed
        if partial_column > 0:
            description += "U" * partial_column + "L"

        # Close the shape
        description += "D" * height + "L" * (full_columns + 1)

    return description

# Read input
N = int(input())

# Generate and print the figure description
result = generate_figure_description(N)
print(result)
