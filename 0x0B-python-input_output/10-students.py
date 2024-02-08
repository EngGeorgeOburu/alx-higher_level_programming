#!/usr/bin/python3
"""
This module defines a class student
"""


class Student:
    """
    Class representing student.
    """
    def __init__(self, first_name,last_name, age):
        """
        Initiliazes a new student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method gets dictionary representing the student
        If attrs is a list of strings, represents only those
        attributess that are included in the list
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

