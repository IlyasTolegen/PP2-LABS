import re

def find_uppercase_followed_by_lowercase(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

print(find_uppercase_followed_by_lowercase("ThisIsAString"))  
print(find_uppercase_followed_by_lowercase("CamelCaseWord")) 
