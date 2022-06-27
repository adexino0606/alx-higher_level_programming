#!/usr/bin/python3
"""
A Rectangle Class with public class attributes, private instance attributes
(width, height), public methods, special methods and static methods
"""


class Rectangle():
    """
    A Rectangle Class with public class attributes,
    private instance attributes width, height, public methods,
    special methods and static methods.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Constructor of the class Rectangle
          Args:
            - width (default = 0): int
            - heigth (default = 0): int
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        """Calculate the area of a Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of a Rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return 0

        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Function to print a Square with the print_symbol
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        final = [str(self.print_symbol) * self.__width
                 for character in range(self.__height)]

        return '\n'.join(final)

    def __repr__(self):
        """Returns an “official” string representation of a Rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter of the property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Getter of the property value
          Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """Getter of the property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Getter of the property value
          Args:
            - value: int
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area
          Args:
            - rect_1: Rectangle
            - rect_2: Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        return rect_2
