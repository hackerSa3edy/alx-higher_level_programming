#!/usr/bin/python3


def max_integer(my_list=[]):
    if not isinstance(my_list, list):
        return None

    list_len = len(my_list)
    if list_len == 0:
        return None

    my_list.sort()
    return my_list[-1]
