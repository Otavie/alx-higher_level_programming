#!/usr/bin/python3
"""Module to add two numbers"""


def add_integer(a, b=98):
    """Method to add two numbers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if a != a:
            raise TypeError("a musr be an integer")
        a = int(a)

    if isinstance(b, float):
        if b != b:
            raise TypeError("b must be an integer")
        b = int(b)

    return a + b
