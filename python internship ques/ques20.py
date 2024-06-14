# This program takes a list of numbers and returns their sum.

def sum_of_list(numbers):
    return sum(numbers)

# Example usage:
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
print("The sum of the list is:", sum_of_list(numbers))
