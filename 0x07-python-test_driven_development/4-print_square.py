#!/usr/bin/python3
"""
4-print_square module

prints a square with the hash (#) character.
"""


def print_square(size):
    """print_square

    Arguments:
        size -- size of the square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print('#', end="")
        print()
