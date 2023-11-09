#!/usr/bin/python3

def roman_to_int(rom_str) -> int:
    if (rom_str is None) or (not isinstance(rom_str, str)):
        return 0

    rom_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    summ = 0
    rom_str_len = len(rom_str)
    for char in range(rom_str_len):
        if char < rom_str_len - 1:
            if rom_int[rom_str[char]] >= rom_int[rom_str[char + 1]]:
                if summ != 0:
                    if (rom_int[rom_str[char - 1]] >= rom_int[rom_str[char]]):
                        summ += rom_int[rom_str[char]]
                else:
                    summ += rom_int[rom_str[char]]
            else:
                summ += (rom_int[rom_str[char + 1]] - rom_int[rom_str[char]])
        else:
            if rom_int[rom_str[char - 1]] >= rom_int[rom_str[char]]:
                summ += rom_int[rom_str[char]]

    return summ
