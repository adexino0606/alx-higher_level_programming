#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Set of test to validate the functionality of the function max integer"""

    def test_doc(self):
        """Validating the documentation in the file"""
        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_max(self):
        """Test normal cases without error"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 5, 1, 1, 3, 1, 2, 1, 5]), 5)

    def test_boolean(self):
        """Test boolean cases without error"""
        self.assertEqual(max_integer([True, False, True]), True)

    def test_strings(self):
        """Test string cases without error"""
        self.assertEqual(max_integer(['h', 'a', 'z']), 'z')

    def test_negatives(self):
        """Test cases with negative integers without error"""
        self.assertEqual(max_integer([-1, -5, -1, -1, -3, -2, -1]), -1)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)

    def test_empty(self):
        """Test cases when the list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_enumber(self):
        """Test cases when the values have an e"""
        self.assertEqual(max_integer([1, 319e520, 5]), 319e520)

    def test_same_number(self):
        """Test cases when all the numbers are equals """
        self.assertEqual(max_integer([1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)

    def test_individual_number(self):
        """Test cases when only exist a number"""
        self.assertEqual(max_integer([1]), 1)


if __name__ == '__main__':
    unittest.main()
