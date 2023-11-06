#!/usr/bin/python3
'''Thois module contain:
Square class - inherits from Rectangle.
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''Rectangle class'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''return area of Square'''
        return (self.__size ** 2)
