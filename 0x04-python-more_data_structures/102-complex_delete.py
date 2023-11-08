#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    temp_dict = a_dictionary.copy()
    for key, val in temp_dict.items():
        if value == val:
            a_dictionary.pop(key)

    return a_dictionary
