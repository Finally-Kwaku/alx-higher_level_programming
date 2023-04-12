#!/usr/bin/python3
"""Creates a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class rectangle that inherits from BaseGeometry"""

    def __init__(self, size):
        """Launch new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
