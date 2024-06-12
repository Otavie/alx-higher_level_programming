#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    A class Square wth a private instance attribute size.

    Attributes:
        __size (int): The size of the square with default value of 0
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

    def area(self):
        """
        Returns the area of the square

        Returns:
            int: The are of the square
        """
        return self.__size * self.__ size
