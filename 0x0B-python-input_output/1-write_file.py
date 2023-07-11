#!/usr/bin/python3
"""A function that writes to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)"""
    with open(filename, 'w', encoding="utf-8") as a_file:
        return a_file.write(text)
