import re

def match_a_followed_by_b(string):
    pattern = r'ab*'
    return bool(re.fullmatch(pattern, string))

print(match_a_followed_by_b("ab"))   
print(match_a_followed_by_b("a"))     
print(match_a_followed_by_b("abb"))   
print(match_a_followed_by_b("ac"))    
