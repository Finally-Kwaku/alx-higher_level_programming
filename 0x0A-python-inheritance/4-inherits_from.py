#!/usr/bin/python3
"""Probes if object is an instance of a class that
inherited from the specified class or not"""


def inherits_from(obj, a_class):
    """
    Return true if the object is an instance of a class that
    inherited (directly or indirectly) from the specified
    class; otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
