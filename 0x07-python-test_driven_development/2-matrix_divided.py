#!/usr/bin/python3
""" Module contain function that divide matrix by div number. """


def matrix_divided(matrix, div):
    """ Function that divide matrix by div number. """

    err_message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(err_message)

    row_sz = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_message)
        row_sz.append(len(row))
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(err_message)

    if row_sz.count(row_sz[0]) != len(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [
        list(map(lambda item: round(item / div, 2), row)) for row in matrix
    ]
