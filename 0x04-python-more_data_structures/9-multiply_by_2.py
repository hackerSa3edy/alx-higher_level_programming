#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    if isinstance(a_dictionary, dict):

        def mul_func(key, value):
            return {key: value * 2}

        new_dict = {}
        for item in map(mul_func, a_dictionary.keys(), a_dictionary.values()):
            new_dict.update(item)

        return new_dict
