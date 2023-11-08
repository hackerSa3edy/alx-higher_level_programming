#!/usr/bin/python3


def common_elements(set_1, set_2):
    if not (isinstance(set_1, set) and isinstance(set_2, set)):
        return []

    return set_1 & set_2
