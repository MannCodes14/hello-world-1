# write a code for plaindrome check
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1] 

# Example usage
if __name__ == "__main__":
    test_string = "A man a plan a canal Panama"
    print(is_palindrome(test_string))       