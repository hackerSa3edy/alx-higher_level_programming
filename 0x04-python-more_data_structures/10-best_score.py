#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None

    big_num = None
    big_num_key = None
    for key in a_dictionary:
        if big_num is None:
            big_num = a_dictionary[key]
            continue

        if a_dictionary[key] >= big_num:
            big_num = a_dictionary[key]
            big_num_key = key

    return big_num_key
