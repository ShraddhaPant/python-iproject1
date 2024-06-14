# This program takes a string input from the user and writes it to a text file

# Get the string input from the user
user_string = input("Enter a string to save to a file: ")

# Open a file in write mode
with open('user_input.txt', 'w') as file:
    # Write the string to the file
    file.write(user_string)

print("Your string has been written to 'user_input.txt'.")

