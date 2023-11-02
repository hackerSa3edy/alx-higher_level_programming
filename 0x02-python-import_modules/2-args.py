#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argsLen = len(sys.argv) - 1
    if argsLen == 0:
        print("{:d} arguments.".format(argsLen))
    elif argsLen == 1:
        print("{:d} argument:".format(argsLen))
    else:
        print("{:d} arguments:".format(argsLen))
    for arg in range(1, argsLen + 1):
        print("{:d}: {:s}".format(arg, sys.argv[arg]))
