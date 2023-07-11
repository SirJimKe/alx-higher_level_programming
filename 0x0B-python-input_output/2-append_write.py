#!/usr/bin/python3
"""A function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """ appends a string and returns the number of characters added"""
    with open(filename, 'a', encoding="utf-8") as a_file:
        return a_file.write(text)
