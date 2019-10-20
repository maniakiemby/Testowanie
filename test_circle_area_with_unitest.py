import unittest
import my_class
import math

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        """Test area when radius >= 0"""           # - docstring (można z nich tworzyć dokumentację)
        self.assertAlmostEqual(my_class.circle_area(1), math.pi)
        self.assertAlmostEquals(my_class.circle_area(2, 1), math.pi * (2.1 ** 2))

    def test_values(self):
        self.assertRaises(ValueError, my_class.circle_area, -2)     # argumenty podajemy po przecinku

    def test_types(self):
        self.assertRaises(TypeError, my_class.circle_area, 3 + 5j)


if __name__ == '__main__':
    unittest.main()
