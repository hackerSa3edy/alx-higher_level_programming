#!/usr/bin/python3
"""1-square module"""


class Square():
    """Square class
    """
    def __init__(self, size=0):
        """Initialze Variables

        Keyword Arguments:
            size -- size of the square (default: {0})

        Raises:
            TypeError: size must be an integer
            ValueError: size bust be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square

        Returns:
            Area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """size getter

        Returns:
            Size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter

        Arguments:
            value -- new size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
