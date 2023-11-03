#!/usr/bin/python3

if __name__ == '__main__':
    import calculator_1 as calc
    import sys

    argsLen = len(sys.argv)
    if argsLen != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    operators = ['+', '-', '*', '/']
    CalcFunc = [calc.add, calc.sub, calc.mul, calc.div]

    if operator not in operators:
        print("Unkown operator. Available operators: +, -, * and /")
        sys.exit(1)

    for op in range(len(operators)):
        if operators[op] == operator:
            c = CalcFunc[op](a, b)
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, c))
            break
