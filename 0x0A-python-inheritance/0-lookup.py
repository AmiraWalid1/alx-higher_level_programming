#!/usr/bin/python3
''' module contain lookup function'''


def lookup(obj):
    '''
    function that returns the list of available attributes
    and methods of an object
    '''
    return dir(obj)
