#!/usr/bin/python3
'''Thois module contain:
Square class - inherits from Rectangle.
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        '''define __init__'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''return area of Square'''
        return (self.__size ** 2)

    def __str__(self):
        '''return string that represent of an object'''
        return f"[Rectangle] {self.__size}/{self.__size}"
