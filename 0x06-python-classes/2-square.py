#!/usr/bin/python3

"""Defines a class Square"""
    
    class Square:

    """
    Class for the attributes and properties of square
    Attributes:
        size: length of a side of a square
    """
    
    def __init__(self, size=0):

        """Class constructor
        Args:
            size: length of a side of a square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
