import math


def calculate_dimensions(diagonal, aspect_ratio=1.0):
    """Calculate width and height from diagonal and aspect ratio"""
    height = diagonal / math.sqrt(1 + aspect_ratio ** 2)
    width = height * aspect_ratio
    return width, height


def can_rectangle_fit(diagonal, aspect_ratio, container_width,
                      container_height):
    """
    Check if a rectangle with given diagonal and aspect ratio can fit inside
    a container rectangle, considering both normal and rotated orientations.

    Args:
        diagonal: Diagonal length of rectangle to fit
        aspect_ratio: Width to height ratio of rectangle to fit
        container_width: Width of the container rectangle
        container_height: Height of the container rectangle

    Returns:
        tuple: (bool, str) - (Whether it fits, Description of how it fits)
    """
    # Calculate dimensions of rectangle to fit
    rect_width, rect_height = calculate_dimensions(diagonal, aspect_ratio)

    # Check normal orientation
    normal_fit = (
                rect_width <= container_width and rect_height <= container_height)

    # Check rotated orientation (90 degrees)
    rotated_fit = (
                rect_height <= container_width and rect_width <= container_height)

    if normal_fit and rotated_fit:
        return True, "Fits in both normal and rotated orientation"
    elif normal_fit:
        return True, "Fits in normal orientation"
    elif rotated_fit:
        return True, "Fits in rotated orientation"
    else:
        return False, "Does not fit in any orientation"
