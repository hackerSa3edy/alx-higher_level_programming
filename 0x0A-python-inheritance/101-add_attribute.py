#!/usr/bin/python3
"""
101-add_attribute module

Initiates add_attribute function that check if the object
allows adding new attributes.
"""


def add_attribute(obj, key, value):
    """add_attribute

    Arguments:
        obj -- The specified object
        key -- new attribute name
        value -- new attribute value

    Raises:
        TypeError: can't add new attribute
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, key, value)
    else:
        raise TypeError("can't add new attribute")
