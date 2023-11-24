#!/usr/bin/python3
"""103-magic_class module

Raises:
    TypeError: radius must be a number

Returns:
    The raduis and the circumference
"""

import math


class MagicClass():
    """MagicClass for 103-magic_class.py task
    """
    def __init__(self, radius=0):
        """Initialize Variables

        Arguments:
            radius -- radius of the MagicClass

        Raises:
            TypeError: radius must be a number
        """
        self.__radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area

        Returns:
            The area
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate the circumference

        Returns:
            The circumference
        """
        return (2 * math.pi) * self.__radius
