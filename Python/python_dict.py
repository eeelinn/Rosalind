# Dictionaries problem

# Given: a string s of length at most 10000 letters
# Return: the num of occurrences of each word in s, where words are
#   case-sensitive, separated by spaces, and the lines in output can
#   be in any order.

import sys

name = sys.argv[1]

wDict = {}

# read in words from file
with open(name, 'r') as f:
    wList = f.read().split()

# calculate occurrence of each word
for w in wList:
    if w in wDict:
        wDict[w] += 1
    else:
        wDict[w] = 1

# print word and occurrence in new file 'output6.txt'
with open('./output6.txt', 'w') as n:
    for key in wDict:
        n.write(key + ' ' + str(wDict[key]) + '\n')


