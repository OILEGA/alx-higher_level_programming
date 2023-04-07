#!/usr/bin/python3
import unittest
from my_module import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 5, 8, 3, 2]), 10)
        self.assertEqual(max_integer([100, 50, 25, 75]), 100)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -8, -3, -2]), -2)
        self.assertEqual(max_integer([-100, -50, -25, -75]), -25)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([10, -5, 8, -3, 2]), 10)
        self.assertEqual(max_integer([-100, 50, -25, 75]), 75)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer("hello")
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three"])

if __name__ == '__main__':
    unittest.main()
