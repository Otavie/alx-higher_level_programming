#!/usr/bin/python3
"""
Defines a class Square
This module contains the definition of the Square class
"""


class Square:
    """
    A class Square wth a private instance attribute size.

    Attributes:
        __size (int): The size of the square with default value of 0
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The length of a side of the square.
            Default value is 0

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter methd for the private attribute __size

        Returns:
            int: The value of the private attribute __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the private attribute __size

        Args:
            value (int): The new value to set for __size

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("sise must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
