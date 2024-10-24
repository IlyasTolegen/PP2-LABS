def check_all_true(tup):
    return all(tup)

# Example usage
tup = (True, True, True)
print(f"Are all elements of the tuple true? {check_all_true(tup)}")

tup2 = (True, False, True)
print(f"Are all elements of the tuple true? {check_all_true(tup2)}")
