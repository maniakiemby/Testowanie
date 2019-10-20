import unittest

import my_functions

class TestAdd(unittest.TestCase):
    def test_add_integer(self):
        """Test that addition of two integers returns the correct result"""
        self.assertEqual(my_functions.add(9, 10), 19)
        self.assertEqual(my_functions.add(0, 5), 5)

    def test_add_float(self):
        """Test that addition of two floats returns the correct result"""
        self.assertAlmostEqual(my_functions.add(2.5, 7.5), 10)
        self.assertAlmostEqual(my_functions.add(17.3, 17.7), 35)

    def test_add_string(self):
        """Test the addition of two strings returns one concatenated string""" # concatenated - konkatenuje (konkatenacja - łączenie stringów)
        self.assertEqual(my_functions.add('abs', 'def'), 'absdef')
        self.assertEqual(my_functions.add('', ''), '')


class TestDivide(unittest.TestCase):
    def test_divide(self):
        """Test if ValueError is raised when needed"""
        self.assertRaises(ValueError, my_functions.divide, 3, 0)



if __name__ == '__main__':
    unittest.main()

"""Zadanie domowe: uzyskać 100% pokrycia testami (coverage)"""
