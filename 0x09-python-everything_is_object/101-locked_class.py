#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    This class prevents the user from dynamically creating new instance attributes
    """
    __slots__ = ['first_name']
