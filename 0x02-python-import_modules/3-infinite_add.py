#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    argsLen = len(argv) - 1
    sumition = 0
    for num in range(1, argsLen + 1):
        sumition += int(argv[num])

    print(sumition)
