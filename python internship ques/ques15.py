# This program  reads data from a CSV file and prints it to the console.

import csv

def read_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

# Example usage:
file_name = input("Enter the CSV file name: ")
read_csv(file_name)
