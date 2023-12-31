#!/usr/bin/python3
'''This module contain:
Rectangle class - inherits from BaseGeometry.
'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle that inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''define init function'''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
