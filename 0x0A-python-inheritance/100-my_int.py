#!/usr/bin/python3
"""MyInt class that inherits from int"""


class MyInt(int):
    """MyInt class  overrides the == and != operators"""

    def __eq__(self, other):
        """Override the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator."""
        return super().__eq__(other)
