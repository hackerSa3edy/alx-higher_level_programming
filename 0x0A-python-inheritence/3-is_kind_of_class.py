#!/usr/bin/python3
"""
3-kind_of_class module

Initiates is_kind_of_class function that checks the object
is an instance of specified class or not.
"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class

    Arguments:
        obj -- specified object
        a_class -- specified class

    Returns:
        True if the object is an instance of, or if the object
        is an instance of a class that inherited from, the
        specified class; otherwise False.
    """
    if obj.__class__ is a_class or issubclass(obj.__class__, a_class):
        return True
    return False
