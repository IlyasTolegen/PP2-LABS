import re

def match_a_followed_by_anything_ending_in_b(string):
    pattern = r'a.*b$'
    return bool(re.fullmatch(pattern, string))


print(match_a_followed_by_anything_ending_in_b("ab"))     
print(match_a_followed_by_anything_ending_in_b("a123b"))  
print(match_a_followed_by_anything_ending_in_b("a"))     

