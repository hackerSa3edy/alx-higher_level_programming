#!/usr/bin/python3
"""
9-rectangel module

Initiates a Rectangle class derrived from BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle

    Arguments:
        BaseGeometry -- parent class
    """
    def __init__(self, width, height):
        """__init__

        Arguments:
            width -- width of the rectangle
            height -- height of the rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """area

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """__str__

        Returns:
            String representation of the rectangle.
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
