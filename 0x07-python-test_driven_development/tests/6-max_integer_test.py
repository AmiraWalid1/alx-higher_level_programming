#!/usr/bin/python3
"""Module to make unit test to max_integer fun in 6-max_integer Module"""


import unittest
max_integer = __import__("6-max_integer").max_integer


class My_test_calss(unittest.TestCase):
    """Class contain test"""
    def test_docstring(self):
        """test docstring of module and function is not empty"""
        self.assertIsNotNone(__import__("6-max_integer").__doc__)
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 1)

        self.assertIsNotNone(max_integer.__doc__)
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        """chek when list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """one posistive & negative element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_max_at_begin(self):
        """test max at begin"""
        self.assertEqual(max_integer([5, 3, 1]), 5)

    def test_max_at_middle(self):
        """test max at middle"""
        self.assertEqual(max_integer([5, 9, 10, 3, 1]), 10)

    def test_max_at_end(self):
        """test max at end"""
        self.assertEqual(max_integer([5, 9, 10, 3, 1, 100]), 100)

    def test_max_at_end(self):
        """test negative numbers"""
        self.assertEqual(max_integer([-2, -4, -9, -5]), -2)
        self.assertEqual(max_integer([-2, -4, -1, -9, -5]), -1)
        self.assertEqual(max_integer([-2, -4, -9, -5, -1]), -1)


if __name__ == "__main__":
    unittest.main()
