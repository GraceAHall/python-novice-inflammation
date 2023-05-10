

import unittest


def add_two_numbers(a, b):
    return a + b


class TestLesson1(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(1, 1)
    
    def test_add_two_numbers(self):
        result = add_two_numbers(1, 2)
        self.assertEqual(result, 3)
