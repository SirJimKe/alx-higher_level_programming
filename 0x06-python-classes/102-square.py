#!/usr/bin/python3
""" class square with instance attribute"""


class Square:
    """ Class that defines a square

    The Square class provides a basic representation of a square

    Attributes:
        __size (int): The size of the square
    Methods:
        area(): returns the current square area
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of a square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares two squares for equality based on their areas.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Compares two squares for inequality based on their areas.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Checks if the area of the current square is greater than another square.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Checks if the area of the current square is greater than or equal to \
        the area of another square.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Checks if the area of the current square is less \
        than the area of another square.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Checks if the area of the current square is less than or \
        equal to the area of another square.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
