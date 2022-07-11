#!/usr/bin/python3
"""
This program define the class Square
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square this class inheritance from Rectangle class.
    """

    # Constructor
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of a Square
        Args:
          - size: int
          - x: int
          - y: int
          - id: int
        """
        super().__init__(size, size, x, y, id)

    # Public Methods
    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square
        Args [Optional each parameter]:
          *args form:
            - Rectangle.update(id:int, size:int, x:int, y:int)\n
          **kwargs form:
            - Rectangle.update(id=int, size=int, x=int, y=int)
        """
        keys = ["id", "size", "x", "y"]
        len_keys, len_args = len(keys), len(args)

        # Maybe refactor because setter of size and use update
        if (args) and (args[0] is not None):
            to_update = len_keys if (len_args > len_keys) else len_args
            for i in range(to_update):
                setattr(self, keys[i], args[i])
        elif (kwargs is not None):
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the representation of the instance Square"""
        return ({
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y,
        })

    # Magic Methods
    def __str__(self):
        """Informal representation of a Square Instance"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))

    # Getters and Setters
    @property
    def size(self):
        """Getter of the private attribute \"size\""""
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Setter of the private attribute size
        Args:
          - value: int
        """
        self.width = value
        self.height = value
