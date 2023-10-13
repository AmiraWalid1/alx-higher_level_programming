#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or isinstance(roman_string, str):
        return 0
    my_dir = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for ch in list(roman_string):
        num += my_dir[ch]
    return num
