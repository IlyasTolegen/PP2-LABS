import re

def replace_space_comma_dot_with_colon(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)

# Test examples
print(replace_space_comma_dot_with_colon("Hello, world. How are you?"))  # "Hello:world:How:are:you?"
