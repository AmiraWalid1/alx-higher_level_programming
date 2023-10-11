#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        for item in lst:
            print("{:d}".format(item), end=(" " if lst[-1] != item else "\n"))
