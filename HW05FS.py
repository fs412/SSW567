""" HW 05: Testing triangle classification """
import unittest

def main():
    """ Input from the user and displaying any errors from the inputs.""" 
    try:
        a = float(input("Enter side 'a' for a triangle rounded to the nearest integer: "))
        b = float(input("Enter side 'b' for a triangle rounded to the nearest integer: ")) 
        c = float(input("Enter side 'c' for a triangle rounded to the nearest integer: "))

    except ValueError:
        print("Please enter a valid numerical digit rounded to the nearest integer.")
        return

    if (a is str):
        return("Please enter a valid numerical digit rounded to the nearest integer.")

    if (b is str):
        return("Please enter a valid numerical digit rounded to the nearest integer.")

    if (c is str):
        return("Please enter a valid numerical digit rounded to the nearest integer.")

    if a <= 0 or b <= 0 or c <= 0:
        return("A triangle's side may not be less than or equal to 0. Please try again.")

    triangle = classify_triangle(a, b, c)
    print(triangle)
    main()

    
def classify_triangle(a, b, c):
    """ Classifying triangles """
    if (a == b == c):
        return("This is an equilateral triangle.")

    elif (a + b <= c) or (a + c <= b) or (b + c <= a):
        return("This is not a triangle.")

    elif (a == b or b == c or a == c) and round(a**2 + b**2) == (c**2):
        return("This is a right, isosceles triangle.")

    elif a == b or b == c or a == c:
        return("This is an isosceles triangle.")

    elif ((a * a == b * b + c * c) or (b * b == a * a + c * c) or (c * c == a * a + b * b)) and (a != b != c):
        return("This is a right, scalene triangle.")

    elif (a != b != c):
        return("This is a scalene triangle.")
    
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
    
