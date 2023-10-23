#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length):
        try:
            new_list.append(my_list_1[idx] / my_list_2[idx])
        except Exception as e:
            new_list.append(0)
            if e.__class__ == TypeError:
                print("wrong type")
            elif e.__class__ == ZeroDivisionError:
                print("division by 0")
            elif e.__class__ == IndexError:
                print("out of range")
    return new_list
