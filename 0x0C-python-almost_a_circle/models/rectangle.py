#!/usr/bin/python3
"""Defines a rectangle module (modules.rectangle)"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that init values for a rectangle object
        Args:
            width:size of the width
            height: size of the height
            x: Variable x
            y:  Variable y
        Return:
            Always nothing
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Method that override str method
        """
        return "[Rectangle] ({id}) {x}/{y} - {width}/{height}".format(
            id=self.id,
            x=self.x,
            y=self.y,
            width=self.width,
            height=self.height
        )

    @property
    def width(self):
        """Getter the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter the value of width
        Args:
            value: The width
        """

        self.validateSetter({'width': value})
        self.__width = value

    @property
    def height(self):
        """Getter the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter the value of height
        Args:
            value: The height
        """

        self.validateSetter({'height': value})
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x

        Arguments:
            value -- The x value
        """
        self.validateSetter({'x': value})
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y

        Arguments:
            value -- The y value
        """
        self.validateSetter({'y': value})
        self.__y = value

    @staticmethod
    def validateSetter(values: dict):
        """Validate the values for the object attributes

        Arguments:
            values -- values as dictionary

        Raises:
            TypeError: <key> must be an integer
            ValueError: <key> must be > 0
            ValueError: <key> must be >= 0
        """
        for key, value in values.items():
            if type(value) is not int:
                raise TypeError(f"{key} must be an integer")
            if key == 'width' or key == 'height':
                if value <= 0:
                    raise ValueError(f"{key} must be > 0")
            elif key == 'x' or key == 'y':
                if value < 0:
                    raise ValueError(f"{key} must be >= 0")

    def area(self):
        """Getter for area"""
        return self.width * self.height

    def display(self):
        """Method that prints to stdout
            Rectangle object with the character #
        """

        char = 0
        if self.height > 0:
            for row in range(self.y):
                print()
            for row in range(self.height):
                for space in range(self.x):
                    print(" ", end="")

                for char in range(self.width):
                    print("#", end="")
                print()
        if char == 0:
            print()

    def update(self, *args, **kwargs):
        """Method that changed the order of arguments for rectangle object
        Args:
           *args: list of arguments
           **kwargs: Dictionary with arguments
        """
        if args == () or args is None:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        elif kwargs == {} or kwargs is None:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[0]           # 1st => id attribute
                elif arg == 1:
                    self.width = args[1]        # 2nd => width attribute
                elif arg == 2:
                    self.height = args[2]       # 3rd => height attribute
                elif arg == 3:
                    self.x = args[3]            # 4th => x attribute
                elif arg == 4:
                    self.y = args[4]            # 5th => y attribute

    def to_dictionary(self):
        """Method that returns a dictionary with
            attributes of the object.
        """

        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
