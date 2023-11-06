#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for n_1 in matrix:
        n_len = len(n_1)
        for n in range(n_len):
            print("{:d}".format(n_1[n]), end='')
            if n != n_len - 1:
                print(" ", end='')
        print()
