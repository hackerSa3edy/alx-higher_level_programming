#!/usr/bin/python3
"""
6-max_integer_test module

Used for testing the aplication with unittest module.
the function is `max_integer`, which returns the big
integer in a list.
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class max_integer_test(unittest.TestCase):
    """max_integer_test

    Arguments:
        unittest -- Base unittest module
    """
    def test_non_valid_data_types(self):
        """tests for exceptions happen with un valid
        data type for the function.
        """
        with self.assertRaises(TypeError):
            max_int(1)
            max_int({3, 5})
            max_int(32.3)
            max_int(None)

    def test_valid_data_types(self):
        """tests the expected result from the max_integer func
        """
        self.assertEqual(max_int(), None)
        self.assertEqual(max_int(1, 1e1000), float('inf'))
        self.assertEqual(max_int(-1e1100, -1e1000), float('-inf'))
        self.assertEqual(max_int(1, -1e1000), 1)
        self.assertEqual(max_int([2, 3, 4, 19.5, 20]), 20)
