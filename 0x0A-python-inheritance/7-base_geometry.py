#!/usr/bin/python3
'''This module contain BaseGeometry class'''


class BaseGeometry:
    ''' BaseGeometry class'''
    def __init__(self):
        '''empty init function'''
        pass

    def area(self):
        '''
        function that raises an Exception with the message
        "area() is not implemented"
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''function that that validates value'''
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
