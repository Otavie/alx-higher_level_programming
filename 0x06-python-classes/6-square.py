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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): The length of a side of the square.
            Default value is 0
            Position (tuple, optional): The position of the square.
            Default value is (0, 0)

        Raises:
            TypeError: If size is not an integer.
            Or position is not a tuple of 2 +ve integers.
            ValueError: If size is less than 0.
            Or position elements are less than 0.
        """
        self.__size = size
        self.__position = position

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
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the private attribute __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the private attribute __position

        Args:
            value (tuple): The new value to set for __position

        Raises:
            TypeError: If value is not a tuple of 2 +ve integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not al(isinstance(num, int) and num>= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Prints the square using the character `#`

        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        else:
            for i in range(self.__size):
                print("#" * self.__size)
