#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w', encoding="UTF8") as my_file:
        return (my_file.write(text))
