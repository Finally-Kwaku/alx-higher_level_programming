#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Defining a student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student.
        If attrs is a list of strings, only attribute names 
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__
