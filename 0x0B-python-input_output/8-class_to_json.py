#!/usr/bin/python3
"""
8-class_to_json module

Initiates class_to_json function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""
import json


def class_to_json(obj):
    """converts object to a dictionary

    Arguments:
        obj -- The specified object

    Returns:
        dict object from the obj object
    """
    return obj.__dict__
