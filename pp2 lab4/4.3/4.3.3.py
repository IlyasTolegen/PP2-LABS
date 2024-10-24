
def area_of_polygon(num_sides, side_length):
    return (num_sides * (side_length ** 2)) / (4 * math.tan(math.pi / num_sides))


num_sides = int(input("Enter the num_sides"))
side_length = int(input("Enter the number: "))

area = area_of_polygon(num_sides, side_length)
print(f"Input number of sides: {num_sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {area:.1f}")
