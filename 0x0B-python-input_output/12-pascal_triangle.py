#!/usr/bin/python3
"""
12-pascal_triangle module

Initiates pascal_triangle function that creates a pascal triangle
"""


def pascal_triangle(n):
    """Creates pascal triangle

    Arguments:
        n -- The triangle's height

    Returns:
        List of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = []
    for row in range(n):
        sublist = []
        sublist.append(1)

        for elmnt in range(row):
            if len(sublist) == row:
                sublist.append(1)
                break

            prevRow = triangle[row - 1]
            tempElmnt = prevRow[elmnt] + prevRow[elmnt + 1]
            sublist.append(tempElmnt)

        triangle.append(sublist)

    return triangle
