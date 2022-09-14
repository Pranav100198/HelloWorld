import unittest

def classify_triangle(a,b,c):
    if a == b == c:
        print("It is an equilateral triangle")

    elif a == b or b == c or c == a:
        print("It is an isosceles triangle")

    elif (a * a + b * b == c * c) or (c * c + b * b == a * a) or (a * a + c * c == b * b):
        print("It is a right Triangle")

    else:
        print("It is a Scalene triangle")


try:
    a = int(input("Enter the first side the triangle: "))
    b = int(input("Enter the second side of the triangle: "))
    c = int(input("Enter the third side of the triangle: "))
    if a > 0 and b > 0 and c > 0:
        classify_triangle(a, b, c)
    else:
        print("Value must be positive and greater than  0")

except ValueError:
    print('Invalid Input, Please enter a valid Value')

