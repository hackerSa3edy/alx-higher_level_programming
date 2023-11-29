#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle():
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Initialize instance variables

        Keyword Arguments:
            width -- width of the rectangle (default: {0})
            height -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter

        Returns:
            The width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Arguments:
            value -- The new value of the width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter

        Returns:
            The height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Arguments:
            value -- The new value of the height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area

        Returns:
            Rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """Rectangle perimeter

        Returns:
            Rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the class

        Returns:
            Readable String
        """
        if self.width == 0 or self.height == 0:
            return ""
        objstr = []
        for _ in range(self.height):
            objstr.append("#" * self.width)
            if _ != self.height - 1:
                objstr.append("\n")

        return "".join(objstr)

    def __repr__(self):
        """Official string representation of the class

        Returns:
            Serialized string
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
