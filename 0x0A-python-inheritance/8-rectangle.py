#!/usr/bin/python3
"""
8-rectangel module

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
