#!/usr/bin/python3


def uniq_add(my_list=[]):
    if not isinstance(my_list, list):
        return my_list

    summition = 0
    for element in set(my_list):
        summition += element

    return summition
