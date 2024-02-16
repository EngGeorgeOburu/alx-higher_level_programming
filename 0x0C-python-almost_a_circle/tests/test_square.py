#!/usr/bin/python3
"""Module for Square Unit test"""
import unittest
from models.base import base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class SquareTest(unittest, TestCase):
    """Test for the Base Class."""
    def setUp(self):
        """Imports a module and instantiates a class"""
        Base._Base_nb_objects = 0

    def tearDown(self):
        """Cleans up after each test_method."""
        pass

    def test_A_class(self):
        """Tests Square class type."""
        self.assertEqual(str(Square),
                "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        """Tests ifsquare inherits the base"""
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        """Tests constructor signature."""
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)
    
    def test_C_construtor_many_args(self):
        """Tests constructor signature."""
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to  positional arguments but 6 was given"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiates(self):
        """Tests for instances"""
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle_height': 10, '_Rectangle_width': 10,
                '_Rectangle_x': 0, '_Rectangle_y':0, 'id': 1}














    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
if __name__ == "__main__":
        unittest.main()

