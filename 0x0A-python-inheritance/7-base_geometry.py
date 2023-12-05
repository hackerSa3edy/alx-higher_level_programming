#!/usr/bin/python3
"""
7-base_geometry module

Initiates BaseGeomtry class.
"""


class BaseGeometry():
    """BaseGeometry

    An empty class.
    """
    def area(self):
        """area

        Raises:
            Exception: area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator

        Arguments:
            name -- variable name
            value -- value of the variable

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater that 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
