#!/usr/bin/python3
"""Creates a Mylist class"""


class MyList(list):
    """
    A class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
