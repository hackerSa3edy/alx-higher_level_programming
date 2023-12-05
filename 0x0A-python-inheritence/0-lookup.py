#!/usr/bin/python3
"""
0-lookup module

Returns a list of all methods and attributes in an object.
"""


def lookup(obj):
    """lookup

    Arguments:
        obj -- The specified object

    Returns:
        List contains all attributes and methods
        in the object
    """
    return dir(obj)
