# Strings and Lists problem

import sys

filename = sys.argv[1]

with open(filename,'r') as f:
    string = f.readline()
    num = f.readline().split()

a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

word1 = string[a:b+1]
word2 = string[c:d+1]

print word1, " ", word2
