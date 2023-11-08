#!/usr/bin/python3
'''module contain append_write function'''


def append_write(filename="", text=""):
    '''function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added'''
    with open(filename, 'a', encoding="UTF8") as my_file:
        return (my_file.write(text))
