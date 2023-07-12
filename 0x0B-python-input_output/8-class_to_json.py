#!/usr/bin/python3
""" a function that returns the dictionary description """


def class_to_json(obj):
    """
    returns the dictionary description with a simple
    data structure for JSON serialization of an object
    """
    description = {}
    for attr, value in vars(obj).items():
        if isinstance(value, (list, dict, str, int, bool)):
            description[attr] = value
    return description
