import re

def insert_spaces_between_capitals(string):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', string)

print(insert_spaces_between_capitals("ThisIsAString"))  
