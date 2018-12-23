# Conditions and Loops problem


# Problem: Given 2 positive ints a and b (a < b < 1000), 
# return the sum of all **odd** integers from [a,b]

import sys

name = sys.argv[1]

#using with automatically closes the file being read
with open(name, 'r') as f:
    args = f.read().split()

a = int(args[0])
b = int(args[1])

nums = range(a,b+1)

#initialize
sum = 0 

for x in nums:
    if(x%2 != 0):
        sum += x

print sum

