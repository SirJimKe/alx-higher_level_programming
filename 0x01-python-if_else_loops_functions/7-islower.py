#!/usr/bin/python3
def islower(c):
    """Checks  for lowercase ascii characters"""
    ascii_value = ord(c)
    return 97 <= ascii_value <= 122
