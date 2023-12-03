#!/usr/bin/python3
"""
5-text_indentation module

Inserts 2 new lines after each occurance of one of those
characters [. ? :]
"""


def text_indentation(text):
    """text_indentation

    Arguments:
        text -- The text to be processed

    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = text
    for delimeter in "?.:":
        new_text = (delimeter + "\n\n").join(
            [line.strip(" ") for line in new_text.split(delimeter)]
            )

    print(new_text, end="")
