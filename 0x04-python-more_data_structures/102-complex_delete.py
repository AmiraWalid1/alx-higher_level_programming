#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lst_deleted_key = []
    for key, val in a_dictionary.items():
        if val == value:
            lst_deleted_key.append(key)
    for key in lst_deleted_key:
        del a_dictionary[key]
    return a_dictionary
