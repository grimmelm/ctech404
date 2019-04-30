import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
for line in lines:
    print(line.split(' ')[0])
