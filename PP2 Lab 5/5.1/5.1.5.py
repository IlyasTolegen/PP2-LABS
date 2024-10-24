import re

def match_a_followed_by_anything_ending_in_b(string):
    pattern = r'a.*b$'
    return bool(re.fullmatch(pattern, string))

# Test examples
print(match_a_followed_by_anything_ending_in_b("ab"))      # True
print(match_a_followed_by_anything_ending_in_b("a123b"))   # True
print(match_a_followed_by_anything_ending_in_b("a"))       # False

