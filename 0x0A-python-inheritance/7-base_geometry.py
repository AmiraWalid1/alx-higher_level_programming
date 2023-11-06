#!/usr/bin/python3
'''This module contain BaseGeometry class'''


class BaseGeometry:
    ''' define class '''
    def __init__(self):
        '''define init function'''
        pass

    def area(self):
        '''define function area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
