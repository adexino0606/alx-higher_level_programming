#!/usr/bin/python3
"""
This program define a Base class for other classes
"""
import csv
import json
import os
import turtle


class Base:
    """
    Base class for future inheritance to Shapes
    """
    # Public Class Attributes
    __nb_objects = 0

    # Constructor
    def __init__(self, id=None):
        """
        Constructor of base Class with id.
        Args:
          - id: int (optional)
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Class Methods
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save in a json file a list of objs (Rectangles or Squares)
        Args:
          - cls: New instance of Base
          - list_objs: List of instances[Squares or Rectangles]
        """
        result = []
        namefile = cls.__name__ + ".json"
        options = ["Rectangle", "Square"]
        name = ""

        if (list_objs is not None and len(list_objs)):
            name = type(list_objs[0]).__name__
            if (name in options):
                if all((type(obj).__name__ == name) for obj in list_objs):
                    result = [obj.to_dictionary() for obj in list_objs]

        with open(namefile, mode="w", encoding="utf-8") as _file:
            _file.write(cls.to_json_string(result))

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance (Rectangle, Square)
        Args:
        - cls: New instance (Square or Rectangle)
        - **dictionary (**kwargs)
        """

        if (cls.__name__ == "Rectangle"):
            dummy = cls(1, 1)
        elif (cls.__name__ == "Square"):
            dummy = cls(1)

        dummy.update(**dictionary)

        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Read a JSON file and create instances from the dicts
        Args:
          - cls: New instance (Square or Rectangle)
        """

        filename = cls.__name__ + ".json"
        json_string = ""
        result = []

        if os.path.exists('./{:s}'.format(filename)):
            with open(filename, mode="r", encoding="utf-8") as _file:
                json_string = _file.read()

            list_of_instances = cls.from_json_string(json_string)
            for instance in list_of_instances:
                result.append(cls.create(**instance))

        return (result)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save in a csv file a list of objs (Rectangles or Squares)
        Args:
          - cls: New instance of Base
          - list_objs: List of instances[Squares or Rectangles]
        """
        result = []
        namefile = cls.__name__ + ".csv"
        options = ["Rectangle", "Square"]
        name = ""

        if (list_objs is not None and len(list_objs)):
            name = type(list_objs[0]).__name__
            if (name in options):
                if all((type(obj).__name__ == name) for obj in list_objs):
                    result = [list(obj.to_dictionary().values())
                              for obj in list_objs]

        with open(namefile, "w", encoding="utf-8") as _file:
            for data in result:
                _file.write(','.join(str(data)[1:-1].split(', ')) + '\n')

    @classmethod
    def load_from_file_csv(cls):
        """
        Read a CSV file and create instances from the dicts
        Args:
          - cls: New instance (Square or Rectangle)
        """

        filename = cls.__name__ + ".csv"
        rectangle_props = ["id", "width", "height", "x", "y"]
        square_props = ["id", "size", "x", "y"]
        result = []

        if os.path.exists("./{:s}".format(filename)):
            with open(filename, mode="r", encoding="utf-8") as _file:
                data_csv = csv.reader(_file)
                if (cls.__name__ == "Rectangle"):
                    for data in data_csv:
                        new_dict = {}
                        for key, value in zip(rectangle_props, data):
                            new_dict[key] = int(value)
                        result.append(cls.create(**new_dict))
                elif (cls.__name__ == "Square"):
                    for data in data_csv:
                        new_dict = {}
                        for key, value in zip(square_props, data):
                            new_dict[key] = int(value)
                        result.append(cls.create(**new_dict))

        return (result)

    # Static Methods
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON representation of a list of dictionaries
        Args:
          - list_dictionaries: list[dict]
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")

        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON to a python type
        Args:
          - json_string: str (that contains list[dict])
        """

        if ((json_string is None) or (len(json_string) == 0)):
            return []

        return (json.loads(json_string))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Takes all instances based with the class Base
        and draws it.
        Args:
          - list_rectangles: Rectangles[]
          - list_squares: Squares[]
        """
        turtle.color('purple', 'lightblue')
        turtle.speed(4)
        turtle.shape('turtle')

        if all(inst.__class__.__name__ == 'Rectangle'
               for inst in list_rectangles):
            for rectangle in list_rectangles:
                turtle.goto(rectangle.x, rectangle.y)
                for _ in range(4):
                    turtle.pendown()
                    turtle.fd(rectangle.width)
                    turtle.rt(90)
                    turtle.fd(rectangle.height)
                    turtle.penup()

        if all(inst.__class__.__name__ == 'Square'
               for inst in list_squares):
            for square in list_squares:
                turtle.goto(square.x, square.y)
                for _ in range(4):
                    turtle.pendown()
                    turtle.fd(square.size)
                    turtle.rt(90)
                    turtle.penup()

        turtle.done()
