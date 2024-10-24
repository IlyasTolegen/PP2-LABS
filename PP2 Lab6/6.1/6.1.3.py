def is_palindrome(string):
    return string == string[::-1]

# Example usage
string = "radar"
print(f"Is '{string}' a palindrome? {is_palindrome(string)}")
