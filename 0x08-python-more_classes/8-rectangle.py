#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle():
    """Rectangle Class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize instance variables

        Keyword Arguments:
            width -- width of the rectangle (default: {0})
            height -- height of the rectangle (default: {0})
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            objstr.append("{:s}".format(self.print_symbol) * self.width)
            if _ != self.height - 1:
                objstr.append("\n")

        return "".join(objstr)

    def __repr__(self):
        """Official string representation of the class

        Returns:
            Serialized string
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Find the biggest rectangle's area

        Arguments:
            rect_1 -- rectangle 1
            rect_2 -- rectangle 2

        Raises:
            TypeError: rect_# must be an instance of Rectangle

        Returns:
            The biggest rectangle's area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __del__(self):
        """Deconstructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
