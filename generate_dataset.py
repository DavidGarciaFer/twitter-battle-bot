"""
File: war.py
Author: David Garcia Fernandez
Date: 27/07/2019
Description: Creates a CSV file with a data set in the supported format.
Input: Plain text file path. Each line of the input file should be formatted as <name>,<message>.
"""

import argparse
import os

parser = argparse.ArgumentParser(description='Create data to start the war.')
parser.add_argument('names_file', help='Text file with names and messages.', type=str)
args = parser.parse_args()

lines = []

# Reading lines from file and removing \n
with open(args.names_file) as f:
    for line in f:
        lines.append(line.replace('\n', ''))

# Sorting in alphabetical order
lines.sort()

os.makedirs('data', exist_ok=True) 

# Writing CSV file
with open('data/war_data.csv', 'w') as f:
    f.write('name,message,day,kills\n')
    for line in lines:
        f.write('{},0,0\n'.format(line))
