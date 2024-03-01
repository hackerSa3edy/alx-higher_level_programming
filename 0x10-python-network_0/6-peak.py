#!/usr/bin/python3
"""
This module contains a function for finding a peak element in a
list of integers.
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

    length = len(list_of_integers)
    center = length // 2
    for switch in range(2):
        for index in range(center + switch, length, 2):
            if is_peak(list_of_integers, index) is not None:
                return list_of_integers[index]
        for index in range(center + switch, length, -2):
            if is_peak(list_of_integers, index) is not None:
                return list_of_integers[index]


def is_peak(arr, index):
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
    if index == length - 1:
        if arr[index] > arr[index - 1]:
            return arr[index]
        return None
    elif index == 0:
        if arr[index] < arr[index + 1]:
            return arr[index]
        return None
    elif (arr[index] >= arr[index - 1]) and (arr[index] >= arr[index + 1]):
        return arr[index]

    return None
