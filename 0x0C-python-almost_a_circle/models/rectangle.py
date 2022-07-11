#!/usr/bin/python3
"""
This program define the class Rectangle
"""
from .base import Base


class Rectangle(Base):
    """
    Class Rectangle this class inheritance from Base class.
    """
    # Constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor of a Rectangle
        Args:
          - width: int
          - height: int
          - x: int
          - y: int
          - id: int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Public Methods
    def area(self):
        """Return the area of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Print the rectangle with the character '#'"""
        print("\n" * self.__y, end="")
        lines = [(" " * self.__x) + ("#" * self.__width)] * self.__height
        print('\n'.join(lines))

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle
        Args [Optional each parameter]:
          *args form:
            - Rectangle.update(id:int, width:int, height:int, x:int, y:int)\n
          **kwargs form:
            - Rectangle.update(id=int, width=int, height=int, x=int, y=int)
        """
        keys = ["id", "width", "height", "x", "y"]
        len_keys, len_args = len(keys), len(args)

        if (args) and (args[0] is not None):
            to_update = len_keys if (len_args > len_keys) else len_args
            for i in range(to_update):
                setattr(self, keys[i], args[i])
        elif (kwargs is not None):
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the representation of the instance Rectangle"""
        return ({
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
        })

    # Magic Methods
    def __str__(self):
        """Informal representation of a Rectangle Instance"""
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
               .format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    # Getters and Setters
    @property
    def width(self):
        """Getter of the private attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Setter of the private attribute width
        Args:
          - value: int
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of the private attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Setter of the private attribute height
        Args:
          - value: int
        """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of the private attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Setter of the private attribute x
        Args:
          - value: int
        """
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of the private attribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Setter of the private attribute y
        Args:
          - value: int
        """
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value
