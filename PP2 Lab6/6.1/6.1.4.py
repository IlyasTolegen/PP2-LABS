import math
import time

def delayed_square_root(number, delay):
    print(f"Waiting for {delay} milliseconds...")
    time.sleep(delay / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"Square root of {number} after {delay} milliseconds is {result}")

# Sample Input
number = 25100
delay = 2123

# Invoke the function
delayed_square_root(number, delay)
