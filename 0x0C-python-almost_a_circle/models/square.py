#!/usr/bin/python3
"""Module that defines a square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that initialized the square
        Args:
            size: side's size of the square
            x: Position on x axis.
            y: Position on y axis.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns the object as string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size

        Arguments:
            value -- The size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that update arguments for square object
        Args:
           *args: list of arguments.
           **kwargs: Dictionary of the arguments.
        """

        if args == () or args is None:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        elif kwargs == {} or kwargs is None:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[0]           # 1st => id attribute
                elif arg == 1:
                    self.size = args[1]        # 2nd => size attribute
                elif arg == 2:
                    self.x = args[2]            # 4th => x attribute
                elif arg == 3:
                    self.y = args[3]            # 5th => y attribute

    def to_dictionary(self):
        """Method that returns the dictionary
            representation of a Square.
        """

        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
