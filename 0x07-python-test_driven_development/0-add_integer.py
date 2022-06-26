#!/usr/bin/python3
"""This program add two integers"""


def add_integer(a, b=98):
    """
    Add two integers
    Args
      a: Int or float
      b: Int or float
    """

    if (type(a) not in [int, float]):
        raise TypeError("a must be an integer")

    if (type(b) not in [int, float]):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
