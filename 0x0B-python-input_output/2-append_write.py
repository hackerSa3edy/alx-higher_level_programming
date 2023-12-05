#!/usr/bin/python3
"""
2-append_write module

Initiates append_write function that handles file operations
"""


def append_write(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
        the number of characters written

    Keyword Arguments:
        filename -- The filename (default: {""})
        text -- The text string (default: {""})
    """
    with open(filename, 'a', encoding="UTF8") as wfile:
        nchars = wfile.write(text)
    return nchars
