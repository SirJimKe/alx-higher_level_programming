#!/usr/bin/python3
"""
A function that takes a filename as input, reads the contents of the JSON file
"""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r') as file:
        obj = json.load(file)
    return obj
