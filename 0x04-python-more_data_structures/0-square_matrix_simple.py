#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for lst in matrix:
        square_lst = []
        for item in lst:
            square_lst.append(item * item)
        square_matrix.append(square_lst)
    return square_matrix
