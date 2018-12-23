# BA1B: Find the Most Frequent Words in a String

# Given: a DNA string Text and an integer k
# Return: all most frequent k-mers in Text (in any order)

import sys

name = sys.argv[1]

with open(name, 'r') as f:
    string = f.readline().strip()
    k = int(f.readline().strip())

kDict = {}

for i in range(len(string)):
    key = string[i:i+k]
    if key in kDict:
        kDict[key] += 1
    else:
        kDict[key] = 1

max_val = max(kDict.values())
max_keys = [k for k, v in kDict.items() if v == max_val] # all keys of max_val

string = ''

for k in max_keys:
    string += k + " " 

print string
