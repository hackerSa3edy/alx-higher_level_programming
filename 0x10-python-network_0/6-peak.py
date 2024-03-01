#!/usr/bin/python3
"""
This module contains a function for finding a peak element in a
list of integers.
"""


def find_peak(list_of_integers=[]):
    """
    Find a peak element in an unordered list of integers using binary search.

    Args:
        list_of_integers (list): An unordered list of integers.

    Returns:
        int: The peak element, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
