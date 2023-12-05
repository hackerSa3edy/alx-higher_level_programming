#!/usr/bin/python3
"""
4-inherits_from module

Initiates inherits_from function which checks if the object
is an instance of a class.
"""


def inherits_from(obj, a_class):
    """inherits_from

    Arguments:
        obj -- specified object
        a_class -- specified class

    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise
        False.
    """
    if issubclass(obj.__class__, a_class) and obj.__class__ is not a_class:
        return True
    return False
