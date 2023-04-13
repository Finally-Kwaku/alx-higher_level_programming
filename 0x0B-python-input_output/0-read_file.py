#!/usr/bin/python3
"""Reads and prints a text file (UTF8) to stdout"""


def read_file(filename=""):
    """Reads and prints a text file (UTF8) to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
