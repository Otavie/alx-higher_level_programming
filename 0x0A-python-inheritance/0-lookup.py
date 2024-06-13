#!/usr/bin/python3


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: object

    Returns:
        list: list of available attributes and metods of an object
    """

    return dir(obj)
