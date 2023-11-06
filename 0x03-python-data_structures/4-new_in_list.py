#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        new_list = my_list.copy()
        list_len = len(my_list)
        if (idx < 0 or idx >= list_len):
            return new_list
        new_list[idx] = element
        return new_list
    return my_list
