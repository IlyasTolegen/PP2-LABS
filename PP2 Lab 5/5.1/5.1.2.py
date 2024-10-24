import re

def match_a_followed_by_two_to_three_b(string):
    pattern = r'ab{2,3}'
    return bool(re.fullmatch(pattern, string))
name=str(input("Enter the string: "))

print(match_a_followed_by_two_to_three_b(name))    
