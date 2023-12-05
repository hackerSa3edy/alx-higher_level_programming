#!/usr/bin/python3
"""
0-read_file module

Initiates read_file function that handles file operations.
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout.

    Keyword Arguments:
        filename -- The file name (default: {""})
    """
    with open(filename, encoding="UTF8") as rfile:
        rdata = rfile.read()
    print(rdata, end="")
