# Working with Files problem

# Given: A file containing at most 10000 lines
# Return: A file containing all the even-numbered lines from the original file

# **Assume 1-based numbering of lines => n%2 == 0 means n is even

import sys

name = sys.argv[1]

i = 1
lines = []

# read in file and only append even-numbered lines
with open(name, 'r') as f:
    for line in f:
        if(i % 2 == 0):
            lines.append(line)
        i += 1

# write even-numbered lines to output file
with open("./output5.txt", 'w') as w:
    for j in lines:
        w.write(str(j) + '\n')


