#!/usr/bin/python3
'''Thois module contain:
Square class - inherits from Rectangle.
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        '''define __init__'''
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''return area of Square'''
        return (self.__size ** 2)

s = Square(13)

print(s)
print(s.area())

