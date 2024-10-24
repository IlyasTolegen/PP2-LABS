import re

def match_a_followed_by_b(string):
    pattern = r'ab*'
    return bool(re.fullmatch(pattern, string))
name=str(input("Enter the name: "))
print(match_a_followed_by_b(name))   
