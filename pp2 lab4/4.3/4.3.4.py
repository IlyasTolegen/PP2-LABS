
def area_of_parallelogram(base, height):
    return base * height

base = int(input("Enter the base: "))
height = int(input("Enter the height: "))

area = area_of_parallelogram(base, height)
print(f"Length of base: {base}")
print(f"Height of parallelogram: {height}")
print(f"Expected Output: {area:.1f}")
