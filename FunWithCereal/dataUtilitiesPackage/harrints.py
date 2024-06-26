#harrints.py

# Name: TJ Harrington
# email: harrints@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is a group assignment thats purpose is to get us to work together
# Brief Description of Module: This Module calls 
# Citations: ChatGBT

from csvUtilitiesPackage.csvUtilities import *
import random

def harrints(csv_file=r'..\dataPackage\cereals.txt'):
    """
    Reads a CSV file, extracts the first word from line 13, prints it, and returns it.

    Args:
    csv_file (str, optional): The path to the CSV file. Defaults to '..\dataPackage\cereals.txt'.

    Returns:
    str: The first word from line 13 of the CSV file.
    """
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        # Skip lines until line 13
        for _ in range(12):
            next(reader, None)
        # Read line 13
        line_13 = next(reader, None)
        # Extract the first word
        if line_13:
            first_word_line_13 = line_13[0].split()[0]
            answer = f"Line 13 of the CSV File has information about {first_word_line_13}"
        return answer
        
            
print(harrints())
