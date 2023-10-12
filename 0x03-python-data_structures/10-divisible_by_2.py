#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_list = []
    for item in my_list:
        if item % 2:
            check_list.append(False)
        else:
            check_list.append(True)
    return check_list
