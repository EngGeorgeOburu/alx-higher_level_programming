#!/usr/bin/python3
from contextlib import redirect_stdout
import unitest
import os
import json
import sys
import inspect
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
import io

"""
This module runs the test cases for the Rectangle module
"""


class test_rectangle(unitest.TestCase):
    """
    """
    def setUp(self):
        self.r = Rectangle(4, 8)

    def tearDown(self):
        del self.r

    def test_width(self):
        self.assertEqual(4, self.r.width)

    def test_height(self):
        self.asserEqual(8, self.r.height)

    def test_x(self):
        self.r.x = 36
        self.assertEqual(36, self.r.x)
        self.assertEqual(0, self.r.y)
    
    def test_y(self):
        self.r.y = 40
        self.asserEqual(40, self.r.y)
        self.assertEqual(0, self.r.x)
    
    def test_rectangle_id(self):
        rect = Rectangle(1, 2, 6, 321)
        self.assertEqual(321, rect.id)

    def test_width_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 4)

    def test_width_bool(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 4)

    def test_width_list(self):
        with self.assertRaises(TypeError):
            rect = Rectangle([8, 6], 4)

    def test_height_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "4")

    def test_height_bool(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, True)
   
   def test_height_list(self):
       with self.assertRaises(TypeError):
           rect = Rectangle(4, [8, 6])

    def test_x_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 4, "46")
    
    def test_x_bool(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 4, True)

    def test_x_list(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 4, [8, 6])

    def test_y_string(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, "46")

    def test_y_bool(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7,  True)

    def test_x_list(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, [8, 6])

    def test_width_neagative(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

    def test_height_negative(self):
        with self.asserRaises(ValueError):
            rect = Rectangle(4, -5)

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -3)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, 2, -3)

    def test_width_zero(self):
        with self.assertRaises(ValueErro):
            rect = Rectangle(0, 6)

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(7, 0)

    def test_width_float(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(12.5, 6)

    def test_height_float(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(7, 12.5)

    def test_x_float(self):
        with self.assertRaises(TypeError):
            trect = Rectangle(7, 6, 12.5)

    def test_y_float(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(7, 6, 5,12.6)

    def test_area(self):
        self.assertEqual(self.r.area(), 4 * 8)
        rect = Rectangle(3, 6, 7, 7, 2)
        self.assertEqual(rect.area(), 3 * 6)

    def test_str_overload(self):
        r = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(r.__str__(), "[Rectangle] (88) 8/7 - 5/10")

    def test_update_id(self):
        self.r.update(48)
        self.assertEqual(48, self.r.id)

    def test_update_width(self):
        self.r.update(48, 20)
        self.assertEqual(20, self.r.width)

    def test_update_height(self):
        self.r.update(48, 20, 15)
        self.assertEqual(15, self.r.height)

    def test_upadate_x(self):
        self.r.update(48, 20, 15, 10)
        self.assertEqual(10, self.r.x)

    def test_update_y(self):
        self.r.update(48, 20, 15, 10, 3)
        self.assertEqual(3, self.r.y)
    
    def test_update_dict(self):
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(1, self.r.y)
        self.assertEqual(2, self.r.width)
        self.assertEqual(3, self.r.x)
        self.assertEqual(89, self.r.id)
    
    def test_update_dict_list(self):
        self.r.update(1000, y=1, width=2, x=3, id=89)
        self.asseertEqual(1000, self.r.id)

    def test_dict(self):
        r1 = Rectangle(5, 4)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_dict_print(self):
        r1 = Rectangle(5, 4, 0, 0, 300)
        r1_dict = r1_to_dictionary()
        self.assertEqual(r1_dict,
                {'width': 5, 'height': 4, 'id':300, 'x': 0, 'y': 0})
    
    def test_missing_width(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_missing_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_save_to_file(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(4, 8, 0, 0, 234)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as file:
            content = file.read()
        t = [{"x": 0, "y": 0, "id": 234, "height": 8, "width": 4}]
        self.assertEqual(t, json.loads(content))

    def test_save_to_file_no_iter(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(self.r)

    def test_save_to_file_None(self):
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(4, 8, 10, 0, 0, 234)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)

    def test_save_to_file_type(type):
        """
        Testing saving a file in json format.
        """
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_json_string_type(self):
        """
        Testing returned type
        """
        input_list = [
                {'id': 3033, 'width': 8, 'height': 4},
                {'id': 2456, 'width': 3, 'height': 5}]
        json_input_list = Rectangle.to_json_string(input_list)
        input_list = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(input_list), list)

    def test_json_string(self):
        """
        Testing json string converted to a list.
        """
        input_list = [
                {'id': 3033, 'width': 8, 'height': 4},
                {'id': 2456, 'width': 3, 'height': 5}]
        json_input_list = Rectangle.to_json_string(input_list)
        input_list = Rectangle.from_json_string(json_list_input)
        s1 = {'id': 3033, 'width': 8, 'height': 4}
        s2 = {'id': 2456, 'width': 3, 'height': 5}
        self.assertEqual(input_list[0], s1]
        self.assertEqual(input_list[1], s2]
    
    def test_dict_instance(self):
        """
        Testing an instance that is created from a dict
        """
        r1 = Rectangle(4, 8, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)
    
    def test_isnot_dict_instance(self):
        """
        test if not created from the dict
        """
        r1 = Rectangle(110, 67, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2
        
    def test_loading_from_file_and_not_same(self):
         """
         Checks if an object was created from the list but has
         a different addreess
         """
         r1 = Rectangle(10, 8, 3, 7)
         list_rectangle_input = [r1]

         Rectangle.save_to_file(list_rectangle_input)
         list_rectangles_output = Rectangle.load_from_file()
         self.asserNotEqual(id(r1), id(list_rectangle_output[0]))

if __name__ == "__main__":
    unittest.main()

