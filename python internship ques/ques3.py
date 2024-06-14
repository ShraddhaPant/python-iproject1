# This program calculates the factorial of a given number

def factorial(n):
    """Return the factorial of a given number n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get input from the user
number = int(input("Enter a number: "))

# Calculate the factorial
fact = factorial(number)

# Display the factorial
print("The factorial of {0} is {1}".format(number, fact))
