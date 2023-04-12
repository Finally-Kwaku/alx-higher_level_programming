#!/usr/bin/python3
"""Probes if object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    A function that returns true if the object is exactly
    an instance of the specified class;
    otherwise False.
    """
    return type(obj) == a_class
