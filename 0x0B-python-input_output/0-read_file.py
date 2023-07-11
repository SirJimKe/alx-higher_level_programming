#!/usr/bin/python3
"""A function that reads a file"""


def read_file(filename=""):
    """Reads a text file (UTF8)"""
    with open(filename, 'r', encoding="utf-8") as a_file:
        print(a_file.read().rstrip())
