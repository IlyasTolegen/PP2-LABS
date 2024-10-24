
def area_of_trapezoid(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = int(input("Enter number height: "))
base1 = int(input("Enter number b1: "))
base2 = int(input("Enter number b2: "))

area = area_of_trapezoid(height, base1, base2)
print(f"Height: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {area}")
