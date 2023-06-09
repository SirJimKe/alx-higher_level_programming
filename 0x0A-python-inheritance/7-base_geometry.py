#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """
    Base class for geometry-related classes.

    Methods:
        area - finds area
        integer_validator - valdates value
    """
    def area(self):
        """Finds area of a figure"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value and assumes name is a string"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
