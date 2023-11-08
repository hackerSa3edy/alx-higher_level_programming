#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not isinstance(matrix, list):
        return matrix

    for l in matrix:
        if not isinstance(l, list):
            return matrix

    new_matrix = []
    for sq in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, sq)))

    return new_matrix
