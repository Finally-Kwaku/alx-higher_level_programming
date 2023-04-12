#!/usr/bin/python3
"""A base geometry class"""


class BaseGeometry:
    """
    A class representing BaseGeometry class
    """
    def area(self):
        """
        method not yet executed.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        verifies if value is an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
