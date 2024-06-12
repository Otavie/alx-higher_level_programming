#!/usr/bin/python3
"""
Module that defines a class Square with a private instance attribute size
"""


class Square:
    """
    A clas Square wth a private instance attribute size.

    Attributes:
        __size (int): The size of the square (private) with default value of 0
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with a given size.

        Args:
            size (int): The size of the square (default is 0)

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
