import math

a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
c = float(input("Enter the length of side 'c': "))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"The area of the triangle is {area}")
