#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string) or (not isinstance(roman_string, str)):
        return 0
    my_dir = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    roman_string = list(roman_string)
    for i in range(len(roman_string) - 1, -1, -1):
        if i + 1 < len(roman_string) and \
         (my_dir[roman_string[i + 1]] > my_dir[roman_string[i]]):
            num -= my_dir[roman_string[i]]
        else:
            num += my_dir[roman_string[i]]
    return num
