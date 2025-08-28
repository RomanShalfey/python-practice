def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 
def get_factorial_input():
    """Prompt the user for a non-negative integer and return it."""
    while True:
        try:
            # Get use from the user
            num = int(input("Enter a non-negative integer for a factorial computation: "))
            # Check if the number is non-negative
            if num >= 0:
                return num
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")
number = get_factorial_input()
print(f"The factorial of {number} is {factorial(number)}")
# factorial_calculator.py
# This script calculates the factorial of a non-negative integer provided by the user.
def test_factorial():
    assert factorial(0) == 1, "Factorial of 0 should be 1"
    assert factorial(1) == 1, "Factorial of 1 should be 1"
    assert factorial(2) == 2, "Factorial of 2 should be 2"
    assert factorial(3) == 6, "Factorial of 3 should be 6"
    assert factorial(4) == 24, "Factorial of 4 should be 24"
    assert factorial(5) == 120, "Factorial of 5 should be 120"
    assert factorial(6) == 720, "Factorial of 6 should be 720"
    print("All tests passed!")