import re

def find_sequences_with_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)

print(find_sequences_with_underscore("lower_case_example"))  
print(find_sequences_with_underscore("some_test_case"))     
