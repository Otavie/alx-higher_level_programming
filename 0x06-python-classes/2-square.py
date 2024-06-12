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
        """
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
