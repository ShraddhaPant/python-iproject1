# This program reads the content of a text file and prints it to the console

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the content of the file
    content = file.read()

# Print the content to the console
print(content)
