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

    def my_print(self):
        """
        Prints the square using '#' character.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("".join(["#" for j in range(self.__size)]))
