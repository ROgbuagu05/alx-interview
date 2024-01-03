#!/usr/bin/python3
"""A function representing Pascal's Triangle"""

def pascal_triangle(n):
    """
    Returns a list representing pascal's triangle of n.

    Args:
    n (integer): The number of rows in the Pascal's triangle.

    Returns:
    An empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for k in range(1, n):
        previous_row = triangle[-1]
        current_row = [previous_row[0]]
        for i in range(1, len(previous_row)):
            current_row.append(previous_row[i-1] + previous_row[i])
        current_row.append(1)
        triangle.append(current_row)

    return triangle
