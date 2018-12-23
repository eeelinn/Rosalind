#for Variables and Some Arithmetic Challenge

import sys #needed to read in cmd line argument

filename = sys.argv[1]
with open(filename, 'r') as f:
    argList = f.read().split()

a = int(argList[0])
b = int(argList[1])

print a * a + b * b
