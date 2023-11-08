#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if not isinstance(my_list, list):
        return my_list
    new_list = my_list.copy()
    for element in range(len(new_list)):
        if new_list[element] == search:
            new_list[element] = replace

    return new_list
