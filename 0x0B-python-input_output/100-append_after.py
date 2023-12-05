#!/usr/bin/python3
"""
100-append_after module

Initiates a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    org_file = ""
    with open(filename, 'r+') as file:
        while (True):
            line = file.readline()
            if not line:
                break
            org_file += line
            if search_string in line:
                org_file += new_string
    with open(filename, 'w') as file:
        file.write(org_file)
