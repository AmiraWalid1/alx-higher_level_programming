#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return 'None'
    mx = my_list[0]
    for item in my_list:
        if item > mx:
            mx = item
    return mx
