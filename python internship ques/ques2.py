# This program checks if the entered number is even or odd

# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("{0} is Even".format(number))
else:
    print("{0} is Odd".format(number))
