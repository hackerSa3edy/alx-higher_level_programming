#!/usr/bin/python3
"""
2-matrix_divided module

Implement a funciton which divides all the elements
of a matrix
"""


def matrix_divided(matrix, div):
    """matrix_divided

    Arguments:
        matrix -- matrix
        div -- division number

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        A new matrix each of its numbers divided by the div number
    """
    mat_size = None
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')

    for lst in matrix:
        if not isinstance(lst, list):
            raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')

        if mat_size is None:
            mat_size = len(lst)
        elif mat_size != len(lst):
            raise TypeError('Each row of the matrix must have the same size')

        for _ in lst:
            if not isinstance(_, (float, int)):
                raise TypeError('matrix must be a matrix (list of lists)\
 of integers/floats')

    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(x / div, 2) for x in lst] for lst in matrix]
