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

    triangle = classify_triangle(a, b, c)
    print(triangle)
  
def classify_triangle(a, b, c):
    """ Classifying triangles """
    if (a == b == c) and (a > 0) and (b > 0) and (c > 0):
        return("This is an equilateral triangle.")
    
    elif not(isinstance(a,int)) and not(isinstance(b,int)) and not(isinstance(c,int)):
        return "Please enter a valid numerical digit rounded to the nearest integer."

    elif (a <= 0) or (b <= 0) or (c <= 0):
        return("A triangle's side may not be less than or equal to 0. Please try again.")

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

if __name__ == '__main__':
    main()
