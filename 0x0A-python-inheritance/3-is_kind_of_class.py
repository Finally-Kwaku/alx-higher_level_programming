#!/usr/bin/python3
"""
Confirms if object is an instance of a class or 
if object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
