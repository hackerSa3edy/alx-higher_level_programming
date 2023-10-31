#!/usr/bin/python3
for first_digit in range(9):
    for second_digit in range(1, 10):
        if (first_digit + 1) <= second_digit:
            if (second_digit == 9 and first_digit == 8):
                print("{:d}{:d}".format(first_digit, second_digit))
            else:
                print("{:d}{:d}".format(first_digit, second_digit), end=", ")
