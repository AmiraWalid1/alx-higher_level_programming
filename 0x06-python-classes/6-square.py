#!/usr/bin/python3
"""1-square.py: define a Square class"""


class Square:
    """Square class defined"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple)) or len(value) != 2 or\
            (not isinstance(value[0], int)) or value[0] < 0 or\
                (not isinstance(value[1], int)) or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print('')
            return
        print("\n" * self.__position[1], end='')
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size)
