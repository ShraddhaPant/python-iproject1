# This program generates the first n numbers in the Fibonacci sequence

def fibonacci(n):
    """Generate the first n numbers in the Fibonacci sequence."""
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Get the number of Fibonacci numbers to generate from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate the Fibonacci sequence
fib_sequence = fibonacci(n)

# Display the Fibonacci sequence
print("The first {0} numbers in the Fibonacci sequence are: {1}".format(n, fib_sequence))
