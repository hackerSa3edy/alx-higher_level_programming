#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not isinstance(matrix, list):
        return matrix

    for l in matrix:
        if not isinstance(l, list):
            return matrix

    new_matrix = matrix.copy()
    return [list(map(lambda x: x ** 2, sq,)) for sq in new_matrix]
