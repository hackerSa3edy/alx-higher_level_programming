#!/usr/bin/python3
for first_digit in range(9):
    for second_digit in range(1, 10):
        if (first_digit + 1) <= second_digit:
            if (second_digit == 9 and first_digit == 8):
                print(f"{first_digit:d}{second_digit:d}")
            else:
                print(f"{first_digit:d}{second_digit:d}", end=", ")
