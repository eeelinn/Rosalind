# BA1A: Compute the Number of Times a Pattern Appears in a Text

# Given: {DNA strings} Text and Pattern
# Return: Count(Text, Pattern)

import sys

name = sys.argv[1]

with open(name, 'r') as f:
    text = f.readline().strip()
    pattern = f.readline().strip()

count = 0
i = 0
pat = len(pattern)
n = len(text) - pat + 1

for i in range(n):
    if text[i:i+pat] == pattern:
        count += 1

print count
