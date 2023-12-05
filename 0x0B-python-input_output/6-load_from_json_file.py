#!/usr/bin/python3
"""
6-fload_from_json_file module

Creates an object from a JSON file
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Arguments:
        my_obj -- The specified object
        filename -- The file name
    """
    with open(filename, 'r') as rJson:
        rdata = json.load(rJson)
    return rdata
