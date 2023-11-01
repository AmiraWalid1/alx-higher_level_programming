#!/usr/bin/python3
""" Module contain text_indentation function. """


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each
    of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ['.', ':', '?']
    line = ""
    for ch in text:
        line += ch
        if ch in special_chars:
            print(line.strip(), end="\n\n")
            line = ""
    if line:
        print(line.strip())
