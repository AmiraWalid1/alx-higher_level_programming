#!/usr/bin/python3
'''This module contain:
Rectangle class - inherits from BaseGeometry.
'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''class Rectangle that inherits from BaseGeometry'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''return area of Rectangle'''
        return (self.__height * self.__width)

    def __str__(self):
        '''return string that represent of an object'''
        return f"[Rectangle] {self.__width}/{self.__height}"
