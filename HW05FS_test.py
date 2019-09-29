from HW05FS import classify_triangle
import unittest
import math

class classify_triangle_test(unittest.TestCase):
    """ Test for classifying triangles."""
    def test_triangle(self):
        self.assertEqual(classify_triangle(3, 3, 3), "This is an equilateral triangle.")
        self.assertEqual(classify_triangle(8, 8, 8), "This is an equilateral triangle.")
        self.assertEqual(classify_triangle(5, 5, 9), "This is an isosceles triangle.")
        self.assertEqual(classify_triangle(6, 6, 9), "This is an isosceles triangle.")
        self.assertEqual(classify_triangle(5, 4, 3), "This is a right, scalene triangle.")
        self.assertEqual(classify_triangle(4, 5, 8), "This is a scalene triangle.")
        self.assertEqual(classify_triangle(6, 7, 8), "This is a scalene triangle.")
        self.assertEqual(classify_triangle(8, 8, 9), "This is an isosceles triangle.")
        self.assertEqual(classify_triangle(11.313708498984,11.313708498984,16), "This is a right, isosceles triangle.")
        self.assertEqual(classify_triangle(3, 3, 9), "This is not a triangle.")
        self.assertNotEqual(classify_triangle(3, 3, 3), "This is not a triangle.")

if __name__ == '__main__':
   unittest.main(exit=False, verbosity=2)