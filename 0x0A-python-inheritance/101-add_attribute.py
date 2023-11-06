#!/usr/bin/python3
'''This module contain: add_attribute class'''


def add_attribute(obj, atrr, value):
    '''
    function that adds a new attribute to an object if it’s possible
    '''
    if hasattr(obj, "__dict__"):
        setattr(obj, atrr, value)
    else:
        raise TypeError("can't add new attribute")
