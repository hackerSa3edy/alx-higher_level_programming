#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    square_matrix = [list(map(lambda x: x ** 2, item)) for item in matrix]
    return square_matrix
