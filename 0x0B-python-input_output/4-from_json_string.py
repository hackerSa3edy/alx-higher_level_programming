#!/usr/bin/python3
"""
4-from_json_string module

Handles json objects
"""
import json


def from_json_string(my_obj):
    """Represent object by a JSON string

    Arguments:
        my_obj -- The specified object

    Returns:
        An object represented by a JSON string
    """
    return json.loads(my_obj)
