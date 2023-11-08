#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding="UTF8") as my_file:
        print(my_file.read())
