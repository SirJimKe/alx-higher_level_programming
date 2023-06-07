#!/usr/bin/python3

def uppercase(str):
    """prints a string in uppercase followed by new line"""
    result = ""
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            result += chr(ord(i) - 32)
        else:
            result += i
    print("{}".format(result))
