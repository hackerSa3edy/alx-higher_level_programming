#!/usr/bin/python3
"""
1-my_list module

Initiates MyList class that derrived from a list class,
and extend it by a print_sorted method.
"""


class MyList(list):
    """MyList

    Arguments:
        list -- Inherited list class
    """
    def print_sorted(self):
        """print_sorted

        print a sorted version of the list.
        """
        print(sorted(self))
