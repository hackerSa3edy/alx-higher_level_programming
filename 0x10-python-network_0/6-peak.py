#!/usr/bin/python3
"""
This module contains a function for finding a peak element in a list of integers.
"""

def find_peak(list_of_integers=[]):
    """
    Find a peak element in a list of integers.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int: The peak element, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    return is_peak(list_of_integers)


def is_peak(arr):
    """
    Helper function to find a peak element in a list.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The peak element, or None if the list is empty.
    """
    if not arr:
        return None

    length = len(arr)
    center = length // 2
    if center == length - 1:
        if arr[center] > arr[center - 1]:
            return arr[center]
        return None
    elif center == 0:
        if arr[center] < arr[center + 1]:
            return arr[center]
        return None
    elif (arr[center] >= arr[center - 1]) and (arr[center] >= arr[center + 1]):
        return arr[center]

    peak = is_peak(arr[center:])
    if peak is None:
        peak = is_peak(arr[:center + 1])
    return peak
