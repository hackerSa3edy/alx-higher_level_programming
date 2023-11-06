#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if isinstance(my_list, list):
        return list(map(check_division_by_2, my_list))


def check_division_by_2(element):
    if element % 2 == 0:
        return True
    else:
        return False
