import re

def find_uppercase_followed_by_lowercase(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)

# Test examples
print(find_uppercase_followed_by_lowercase("ThisIsAString"))  # ['This', 'Is', 'A']
print(find_uppercase_followed_by_lowercase("CamelCaseWord"))  # ['Camel', 'Case', 'Word']
