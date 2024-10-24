def count_upper_lower(string):
    upper_count = sum(1 for c in string if c.isupper())
    lower_count = sum(1 for c in string if c.islower())
    return upper_count, lower_count


string=str(input("Enter the string: "))
upper, lower = count_upper_lower(string)
print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")
