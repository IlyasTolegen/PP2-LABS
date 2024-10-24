import re

def insert_spaces_between_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

# Test examples
print(insert_spaces_between_capitals("ThisIsAString"))  # "This Is A String"
