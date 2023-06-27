#!/usr/bin/python3
""" class square with instance attribute"""


class Square:
    """ Class that defines a square

    The Square class provides a basic representation of a square

    Attributes:
        __size (int): The size of the square
    Methods:
        None
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
