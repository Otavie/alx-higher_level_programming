#!/usr/bin/python3

"""Defines a class Square"""
    
    class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size(int, optional): The length of a side of the square.
            Default value is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
