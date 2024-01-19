#!/usr/bin/python3
''' This Module contain pascal_triangle function'''


def pascal_triangle(n):
    '''
    function that returns a list of lists of integers representing
    the Pascal’s triangle of n
    '''
    if n <= 0:
        return []

    My_list = []
    for i in range(n):
        # First element = 1
        sublist = [1]

        for j in range(1, i):
            sublist.append(My_list[i-1][j] + My_list[i-1][j-1])

        # Last element = 1
        if i != 0:
            sublist.append(1)

        My_list.append(sublist)

    return My_list
