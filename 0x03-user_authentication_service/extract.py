#!/usr/bin/env python3

import sys
import os

# Function to extract filenames and content
def extract_content(filename, lines):
    found_alex = False
    for line in lines:
        if "bob@dylan" in line and "cat" in line:
            filename = line.split()[-1]
            found_alex = True
        elif found_alex:
            if "bob@dylan" in line:
                found_alex = False
                continue
            else:
                with open(filename, "a") as file:
                    file.write(line)

# Check if file name is provided as argument
if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

# Get the file name from command line argument
filename = sys.argv[1]

# Check if file exists
if not os.path.isfile(filename):
    print("File not found:", filename)
    sys.exit(1)

# Read the content of the file
with open(filename, "r") as file:
    lines = file.readlines()

# Extract filenames and content
extract_content(filename, lines)

