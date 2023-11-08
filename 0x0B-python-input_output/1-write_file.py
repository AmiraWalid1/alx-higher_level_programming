#!/usr/bin/python3
'''module contain write_file function'''


def write_file(filename="", text=""):
    '''
    function that writes a string to a text file (UTF8) and
    returns the number of characters written
    '''
    with open(filename, 'w', encoding="UTF8") as my_file:
        return (my_file.write(text))
