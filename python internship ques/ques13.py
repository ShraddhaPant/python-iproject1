#This program asks the user for their birth year and calculates their age

from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    return current_year - birth_year

# Example usage:
birth_year = int(input("Enter your birth year: "))
print("Your age is:", calculate_age(birth_year))
