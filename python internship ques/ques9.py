# This program checks if a substring is present in a given string

# Get the main string from the user
main_string = input("Enter the main string: ")

# Get the substring to check
substring = input("Enter the substring to check for: ")

# Check if the substring is present in the main string
if substring in main_string:
    print("The substring '{0}' is present in the main string.".format(substring))
else:
    print("The substring '{0}' is NOT present in the main string.".format(substring))
