#!/usr/bin/python3
"""
This is module 9-student
"""


class Student:
    """
    Define a student by first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student instance with the given attributes.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionaryrepresentation of a student instance.
        """
        return self.__dict__
