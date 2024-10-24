from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

result = multiply_list(numbers)

print(f"The product of the list is: {result}")

