#!/usr/bin/python3
"""1-square module"""


class Square():
    """Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Values

        Keyword Arguments:
            size -- size of the square (default: {0})
            position -- starting point to print the square (default: {(0, 0)})

        Raises:
            TypeError: size must be an integer
            ValueError: size bust be >= 0
            TypeError: position must be a tuple of 2 positive integers
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not (isinstance(position, tuple) and len(position) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(x >= 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    def __str__(self):
        """str representation for the instance of Square

        Returns:
            square as dash string
        """
        char = 0
        Square_as_str = ""
        if self.size > 0:
            for row in range(self.position[1]):
                Square_as_str += "\n"
        for row in range(self.size):
            for space in range(self.position[0]):
                Square_as_str += " "

            for char in range(self.size):
                Square_as_str += "#"
            if row != self.size - 1:
                Square_as_str += "\n"
        return Square_as_str

    def my_print(self):
        """print the square
        """
        char = 0
        if self.size > 0:
            for row in range(self.position[1]):
                print()
        for row in range(self.size):
            for space in range(self.position[0]):
                print(" ", end="")

            for char in range(self.size):
                print("#", end="")
            print()
        if char == 0:
            print()

    @property
    def position(self):
        """position getter

        Returns:
            The position values
        """
        return self.__position

    @position.setter
    def position(self, value):
        """position setter

        Arguments:
            value -- the new position values

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
