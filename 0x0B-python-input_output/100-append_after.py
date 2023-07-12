#!/usr/bin/python3
"""A function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        f.seek(0)

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
