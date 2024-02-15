#!/usr/bin/python3
"""
This module will contain a class that serves aas the base for the other classes
"""
import csv
import json
import os
import turtle


class Base:
    """Represents base of all classes created"""
    _nb_object = 0

    def __init__(self, id=None):
        """ """
        if id is not None:
            self.id = id
        else:
            Base._nd_objects += 1
            self.id = Base._nb_objects

        @staticmethod
        def to_json_string(list_dictionaries):
            """Returns the JSON representation of list_ditionaries"""
            if list_dictionaries is None or list_dictionaries == []:
                return "[]"
            if (type(list_dictionaries) != list or not
                    all(type(i) == dict for i in list_dictionaries)):
                raise TypeError("list_dictionaries must be a list of dictionaries")
            return json.dumps(list_dictionaries):
        @classmethod
        def save_to_file(cls, list_obj):
             """Save JSON representation to file"""
             file_name = cls._name_+ ".json"
             with open(file_name, "w") as jsonfile:
                 if list_objs is None:
                     jsonfile.write("[]") 
                 else:
                     list_dicts = [0.to_dictionary() for o in list_objs]
                     jsonfile.write(Base.to_json_string(list_dicts))
                
        @staticmethod
        def from_json_string(json_string):
            """Returns list of JSON string representation"""
            json_string_list = []

            if json_string is not None and json_string != '':
                if type(json_string) != str:
                    raise TypeError("json_string must be a string")
                json_string_list = json.loads(json_string)

                return json_string_list

        @classmethod
        def create(cls, **dictionary):
            """
            Returns:
                Class instance from a dictionary of attributes.
            Args:
                **dictionary (dict): Key/value pairs of attributes.
            """
            if dictionary and dictionary != {}:
                if cls._name_ == "Rectangle":
                    new = cls(1, 1)
                else:
                    new = cls(1)
                new.update(**dictionary)
                return new

        @classmethod
        def load_from_file(cls):
            """
            Return lists of classes that are instantiated from JSON strings file,
            <cls._name_>.json, the document to Read from
            """
            name_of_file = str(cls._name_) + ".json"
            try:
                with open(name_of_file, "r") as jsonfile:
                    list_dicts = Base.from_json_string(jsonfile.read())
                    return [cls.create(**d) for d in list_dicts]
                except IOError:
                    return []

        @classmethod
        def save_to_file_csv(cls,list_objs):
            """
            Writing to the CSV serialization of a list of objects into a file.
            """
            name_of_file = cls._name_ + ".csv"
            with open(filename, "w", newline="") as csvfile:
                if list_objs is None or list_objs == []:
                    csvfile.write("[]")
                else:
                    if cls._name_ == "Rectangle":
                        name_of_field = ["id", "width", "height", "x", "y"]
                    else:
                        name_of_field = ["id", "size", "x", "y"]
                    writer = scv.Dictwriter(csvfile, name_of_field=name_of_fieldname)
                    for obj in list_objs:
                        writer.writerow(obj.to_dictionary())

        @classmethod
        def load_from_file_csv(cls):
            """Return a list classes instantiated from a csv file."""
            name_of_file = cls._name_+ ".csv"
            try:
                with open(filename,"r", newline="") as csvfile:
                    if cls._name_ == "Rectangle":
                        name_of_field = ["id", "width", "height", "x", "y"]
                    else:
                        name_of_field = ["id", "width", "height", "x", "y"]
                    list_dicts = csv.DictReader(csvfile, name_of_field=name_of_field)
                    list_dicts = [dict([k, int(v)] for k, v in d.items())
                            for d in list_dicts]
                    return [cls.create(**d) for d in list_dicts]
                except IOError:
                    return []
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        """
        turtle = turtle.Turtle()
        turtle.screen.bgcolor("#b7312c")
        turtle.pensize(3)
        turtle.shape("turtle")

        turtle.color("#fffff")
        for rectangle in list_rectangle:
            turtle.showturtle()
            turtle.up()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.down()
            for i in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.color("#b5e3d8")
        for square in list_squares:
            turtle.showturtles()
            turtle.up()
            turtle.goto(square.x, square.y)
            turtle.down()
            for i in range(2):
                turtle.forward(square.width)
                turtle.left(90)
                turtle.forward(square.height)
                turtle.left(90)
            turtle.hideturtle()

        turtle.exitonclick()


