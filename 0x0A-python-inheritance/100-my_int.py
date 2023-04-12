#!/usr/bin/python3
"""A class MyInt that inherits from int"""


class MyInt(int):
    """Upend int operators == and !=."""

    def __eq__(self, value):
        """Counter == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Counter != operator with == behavior."""
        return self.real == value
