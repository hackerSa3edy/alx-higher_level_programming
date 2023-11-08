#!/usr/bin/python3


def simple_delete(a_dictionary, keys=""):
    if isinstance(a_dictionary, dict):
        if a_dictionary.get(keys):
            a_dictionary.pop(keys)

        return a_dictionary
