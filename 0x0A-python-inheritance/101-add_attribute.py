#!/usr/bin/python3
""" adds a new attribute to an object"""


def add_attribute(obj, attribute_name, attribute_value):
    """Adds new attribute to the object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, attribute_value)
