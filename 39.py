# Volume of a Cube
side_length = float(input("Enter the side length of the cube: "))
cube_volume = side_length**3
print(f"The volume of the cube is {cube_volume:.2f} cubic units")

# Volume of a Sphere
radius = float(input("Enter the radius of the sphere: "))
sphere_volume = (4/3) * 3.14159265359 * radius**3
print(f"The volume of the sphere is {sphere_volume:.2f} cubic units")

# Volume of a Cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
cylinder_volume = 3.14159265359 * radius**2 * height
print(f"The volume of the cylinder is {cylinder_volume:.2f} cubic units")
