#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order"""
    new_list = my_list[::-1]
    for num in new_list:
        print("{:d}".format(num))
