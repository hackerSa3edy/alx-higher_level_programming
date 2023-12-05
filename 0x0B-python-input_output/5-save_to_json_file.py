#!/usr/bin/python3
"""
5-save_to_json_file module

Writes an object to a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation.

    Arguments:
        my_obj -- The specified object
        filename -- The file name
    """
    with open(filename, 'w') as wJson:
        json.dump(my_obj, wJson)
