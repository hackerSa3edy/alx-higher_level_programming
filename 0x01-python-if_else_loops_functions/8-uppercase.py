#!/usr/bin/python3
def uppercase(string):
    toUpper = 0
    for char in string:
        if ord(char) in range(97, 123):
            toUpper = 32
        print("{:c}".format(ord(char) - toUpper), end="")
        toUpper = 0
    print()
