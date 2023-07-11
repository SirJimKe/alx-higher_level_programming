#!/usr/bin/python3
"""Defines square class that inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with square properties"""
    def __init__(self, size):
        """constructor"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

        def area(self):
            """finds area of a square """
            return self.__size ** 2

        def __str__(self):
            """string"""
            return "[Square] {}/{}".format(self.__size, self.__size)
