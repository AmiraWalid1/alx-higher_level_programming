#!/usr/bin/python3
'''
This module contain:
  BaseGeometry class
'''


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
