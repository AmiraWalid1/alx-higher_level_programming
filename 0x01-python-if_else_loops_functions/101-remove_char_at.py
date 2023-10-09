#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ''
    idx = 0
    for ch in str:
        if idx != n:
            new_str += ch
        idx += 1
    return new_str
