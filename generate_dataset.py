"""
File: war.py
Author: David Garcia Fernandez
Date: 27/07/2019
Description: Creates a CSV file with a data set in the supported format.
Input: Plain text file path. Each line of the input file should be formatted as <name>,<message>.
"""

lines = []

# Reading lines from file and removing \n
with open('data/harry_potter.txt') as f:
    for line in f:
        lines.append(line.replace('\n', ''))

# Sorting in alphabetical order
lines.sort()

# Writing CSV file
with open('data/war_data.csv', 'w') as f:
    f.write('name,message,day,kills\n')
    for line in lines:
        f.write('{},0,0\n'.format(line))
