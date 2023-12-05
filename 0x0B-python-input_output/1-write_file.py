#!/usr/bin/python3
"""
1-write_file module

Initiates write_file function that handles file operations
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
        the number of characters written

    Keyword Arguments:
        filename -- The filename (default: {""})
        text -- The text string (default: {""})
    """
    with open(filename, 'w', encoding="UTF8") as wfile:
        nchars = wfile.write(text)
    return nchars
