#!/usr/bin/python3
"""
3-to_json_string module

Handles json objects
"""
import json


def to_json_string(my_obj):
    """JSON representation of an object

    Arguments:
        my_obj -- The specified object

    Returns:
        JSON representation of an object
    """
    return json.dumps(my_obj)
