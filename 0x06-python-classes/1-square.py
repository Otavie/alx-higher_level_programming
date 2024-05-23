#!/usr/bin/python3

"""Defines a class Square"""

class Square:

    """
    This class represents a Square.

    Attributes:
        size (int): The length of a side of the square
    """

    def __init__(self, size):
        
        """
        Initilaize a new instance of the Square class.

        Args:
            size(int): The length of a side of the square

        Returns:
            None
        """

        self.__size = size
