import math

def segment_area(radius, angle_degrees):
    return (angle_degrees / 360) * math.pi * (radius ** 2)

# Example usage:
radius = 8
angle_degrees = 60
area = segment_area(radius, angle_degrees)
print(f"The area of the segment is {area} square units.")
