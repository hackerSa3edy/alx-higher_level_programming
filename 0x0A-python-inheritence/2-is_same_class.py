#!/usr/bin/python3
"""
2-is_same_class module

Initiates is_same_class function that checks if the
object exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """is_same_class

    Arguments:
        obj -- specified object
        a_class -- specified class

    Returns:
        True if the object is exactly an instance of
        the specified class
    """
    if obj.__class__ is a_class:
        return True
    return False
