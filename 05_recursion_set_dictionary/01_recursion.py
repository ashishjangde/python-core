# Recursion in Python
# Recursion is the process of defining something in terms of itself.
# A physical world example would be to place two parallel mirrors facing each other.
# Any object in between them would be reflected recursively.

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    # This is where the recursion stops
    if (n == 0 | n == 1):
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        # Function calls itself with a smaller value until it reaches base case
        # Example for n=5: 5 * factorial(4) -> 5 * 4 * factorial(3) -> 5 * 4 * 3 * factorial(2) -> 5 * 4 * 3 * 2 * factorial(1) -> 5 * 4 * 3 * 2 * 1
        return n * factorial(n - 1)


# Test the factorial function with n = 5
n = 5
print(f"Factorial of {n} is {factorial(n)}")  # Should output: Factorial of 5 is 120