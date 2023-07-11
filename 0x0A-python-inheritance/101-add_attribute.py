#!/usr/bin/python3
def add_attribute(obj, attribute_name, attribute_value):
    """Add a new attribute to the object if possible."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute_name, attribute_value)
