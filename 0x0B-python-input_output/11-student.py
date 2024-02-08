#!/usr/bin/python3
"""
This module defines a class 11-student
"""


class Student:
    """
    Class representation of student.
    """

    def __inti__(self,first_name, last_name, age):
        """
        Initializes a new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self,attrs=None):
        """
        This methods gets dictionary representation of the student
        if the attrs is alist of strings, represents only those attributes
        inlcuded in the list
        """
        if (type(attrs) == list and
                all(type(element == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Rplaces all attributes of the student.
        """
        for i, j in json.items():
            setatrr(self, i, j)



