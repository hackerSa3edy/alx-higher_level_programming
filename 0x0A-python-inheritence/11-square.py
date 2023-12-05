#!/usr/bin/python3
"""
11-square module

Initiates a Square class derrived from Rectangle parent class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square

    Arguments:
        Rectangle -- parent class
    """
    def __init__(self, size):
        """__init__

        Arguments:
            size -- size of the square
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """__str__

        Returns:
            String representation for the Square class
        """
        return '[Square] {}/{}'.format(self.__size, self.__size)
