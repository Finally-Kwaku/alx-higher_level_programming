#!/usr/bin/python3
"""Creates a square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area"""
        return self.__size ** 2

    def __str__(self):
        """returns the print() and str() description of rectangle"""
        return "[Square] {}/{}".format(self.__size, self.__size)
