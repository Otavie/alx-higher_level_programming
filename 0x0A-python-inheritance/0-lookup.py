#!/usr/bin/python3
"""Returns the function lookup(obj)"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: object

    Returns:
        list: list of available attributes and metods of an object
    """

    return dir(obj)
