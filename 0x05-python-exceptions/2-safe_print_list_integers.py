#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end="")
        except (ValueError, TypeError):
            pass
        else:
            length += 1

    return length
