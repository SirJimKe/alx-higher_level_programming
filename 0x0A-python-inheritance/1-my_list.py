#!/usr/bin/python3
""" class MyList that inherits form list """


class MyList(list):
    """
    A custom list class that inherits from list

    Methods:
         print_sorted - prints the list
    """


    def print_sorted(self):
        """
        prints the list in ascending sorted order
        """
        print(sorted(self))
