def get_optimal_dimensions(n: int) -> tuple:
    """
    Calculate optimal dimensions for a figure containing exactly n squares
    with the shortest possible outline path.

    Args:
        n: Number of squares required inside the figure

    Returns:
        Tuple of (width, height, extra_blocks)
    """
    def calculate_path_length(w: int, h: int, extra: int) -> int:
        """Calculate the length of path needed for given dimensions"""
        # Basic rectangle perimeter
        base_length = 2 * (w + h)
        # Add extra moves needed for additional blocks
        if extra > 0:
            # Each extra block typically needs 2 additional moves
            extra_moves = extra * 2
            return base_length + extra_moves
        return base_length

    def is_better_solution(new_w: int, new_h: int, new_extra: int,
                           best_w: int, best_h: int, best_extra: int) -> bool:
        """Compare two solutions to determine if new one is better"""
        new_path = calculate_path_length(new_w, new_h, new_extra)
        old_path = calculate_path_length(best_w, best_h, best_extra)
        return new_path < old_path

    # Initialize with square root as starting point
    from math import isqrt
    base = isqrt(n)

    best_width = base
    best_height = base
    best_extra = n - (base * base)

    # Try different rectangular arrangements
    for width in range(max(1, base - 5), base + 6):
        height = n // width
        extra = n - (width * height)

        if extra >= 0 and is_better_solution(width, height, extra,
                                             best_width, best_height, best_extra):
            best_width = width
            best_height = height
            best_extra = extra

    return best_width, best_height, best_extra


def generate_path(width: int, height: int, extra: int) -> str:
    """
    Generate the path description using G(up), D(down), L(left), P(right)

    Args:
        width: Width of the main rectangle
        height: Height of the main rectangle
        extra: Number of extra blocks to add

    Returns:
        String containing the path description
    """
    path = []

    # Draw main rectangle
    path.extend(['G'] * height)  # Up
    path.extend(['P'] * width)   # Right
    path.extend(['D'] * height)  # Down
    path.extend(['L'] * width)   # Left

    # Add extra blocks if needed
    if extra > 0:
        # Add extra blocks along the left side
        for i in range(extra):
            path.extend(['G', 'P', 'D', 'L'])

    return ''.join(path)


def solve(n: int) -> str:
    """
    Main solving function

    Args:
        n: Number of squares required inside the figure

    Returns:
        Shortest path description that encloses exactly n squares
    """
    if n < 1:
        raise ValueError("Number of squares must be positive")

    width, height, extra = get_optimal_dimensions(n)
    return generate_path(width, height, extra)

# Example usage


def main():
    test_cases = [3, 4, 12, 13, 16]

    for n in test_cases:
        path = solve(n)
        print(f"\nFor n = {n}:")
        print(f"Path: {path}")
        print(f"Path length: {len(path)}")


if __name__ == "__main__":
    main()
