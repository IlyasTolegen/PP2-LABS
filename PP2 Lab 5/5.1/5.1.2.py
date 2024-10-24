import re

def match_a_followed_by_two_to_three_b(string):
    pattern = r'ab{2,3}'
    return bool(re.fullmatch(pattern, string))

# Test examples
print(match_a_followed_by_two_to_three_b("abb"))    # True
print(match_a_followed_by_two_to_three_b("abbb"))   # True
print(match_a_followed_by_two_to_three_b("abbbb"))  # False
print(match_a_followed_by_two_to_three_b("ab"))     # False
