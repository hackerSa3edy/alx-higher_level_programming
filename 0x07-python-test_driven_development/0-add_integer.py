#!/usr/bin/python3
"""
add_integer module

Adds two numbers whether float or int and return an integer
summation of them.
"""


def add_integer(a, b=98):
    """add_integer

    Arguments:
        a -- number one

    Keyword Arguments:
        b -- number two (default: {98})

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        Summation of the two numbers.
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
