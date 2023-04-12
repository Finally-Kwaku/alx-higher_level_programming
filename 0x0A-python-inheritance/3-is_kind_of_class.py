#!/usr/bin/python3
"""Determines if an object is from same class
or inherited from a class"""


def is_kind_of_class(obj, a_class):
    """
    Return true if the object is an instance of a class;
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
