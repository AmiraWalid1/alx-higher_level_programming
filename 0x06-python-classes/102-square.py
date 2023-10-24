#!/usr/bin/python3
"""1-square.py: define a Square class"""


class Square:
    """Square class defined"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size ** 2)

    def __eq__(self, other) -> bool:
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        return self.area() != other.area()

    def __lt__(self, other) -> bool:
        return self.area() < other.area()

    def __gt__(self, other) -> bool:
        return self.area() > other.area()

    def __le__(self, other) -> bool:
        return self.area() <= other.area()

    def __ge__(self, other) -> bool:
        return self.area() >= other.area()
