#!/usr/bin/python3
'''module contain read_file function'''


def read_file(filename=""):
    '''function that reads a text file (UTF8) and prints it to stdout'''
    with open(filename, 'r', encoding="UTF8") as my_file:
        print(my_file.read())
