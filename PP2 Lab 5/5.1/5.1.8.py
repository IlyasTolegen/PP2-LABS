import re

def split_at_uppercase(string):
    return re.findall(r'[A-Z][^A-Z]*', string)

# Test examples
print(split_at_uppercase("ThisIsAString"))  # ['This', 'Is', 'A', 'String']
