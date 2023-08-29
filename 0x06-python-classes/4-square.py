#!/usr/bin/python3
class Square:
    """
    Class that defines the properties of square based on 3-square.py

    Attributes:
        size: size of a side of the square
    """

    def __init__(self, size=0):

        """Create a class constructor
        Args:
            size: size of a side of the square
        """

        self.__size = size

    @property
    def size(self):
        """Returns the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """
        Property Setter for size

        Args:
            value: size of a side of the square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """Calculates and returns the area of the square"""

        return self.__size * self.__size
