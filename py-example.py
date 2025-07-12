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

# add a function of factorial
def factorial(n):   
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Example usage
if __name__ == "__main__":              
    num = 5
    print(f"Factorial of {num} is {factorial(num)}")    