#!/usr/bin/python3
"""
This program define a LockedClass that you only can set
the attribute first_name
"""


class LockedClass():
    """
    This class is Locked and you can only put the attribute first_name
    """

    __slots__ = ('first_name', )
