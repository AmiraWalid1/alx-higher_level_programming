#!/usr/bin/python
def no_c(my_string):
    new_str = ''
    for ch in my_string:
        if ch not in ['c', 'C']:
            new_str += ch
    return new_str
