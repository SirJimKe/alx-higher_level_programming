#!/usr/bin/python3
""" This is class Rectangle"""


class Rectangle:
    """ Class that defines a rectangle

    The Rectangle class provides basic representation of a rectangle

    Attributes:
        __width: width of the rectangle
        __height: height of the rectangle
    Methods:
        area: finds area
        perimenter: finds perimeter
    """
    def __init__(self, width=0, height=0):
        """ Instatiation of width and height"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Retrives width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width mush be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """ Prints a rectange using '#' """
        if self.__height == 0 or self.__width == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += '#' * self.__width + '\n'
        return rect.rstrip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
