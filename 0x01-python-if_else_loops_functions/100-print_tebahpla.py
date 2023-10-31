#!/usr/bin/python3
toUpper = 0
for char in range(122, 96, -1):
    if (char % 2 != 0):
        toUpper = 32
    print(f"{chr(char - toUpper)}", end="")
    toUpper = 0
